"""
Micro Print PDF Arranger
========================
Yeh script aapka normal PDF leti hai aur ek naya PDF banati hai jisme pages
is tarah arrange hote hain ki duplex micro-print (4-up) karne pe har cut-out
ke front-back pe sahi consecutive pages aayein.

Layout (Portrait A4, 4 pages per side):
  Front Side:          Back Side (Long-Edge Flip):
  ┌────┬────┐          ┌────┬────┐
  │ TL │ TR │          │ TL │ TR │
  ├────┼────┤          ├────┼────┤
  │ BL │ BR │          │ BL │ BR │
  └────┴────┘          └────┴────┘

Pairing after cut (long-edge flip = left-right mirror):
  Front TL ↔ Back TR   (Page N front, Page N+1 back)
  Front TR ↔ Back TL
  Front BL ↔ Back BR
  Front BL ↔ Back BL... corrected below

For each group of 8 pages:
  Front:  1, 3, 5, 7  (TL, TR, BL, BR)
  Back:   4, 2, 8, 6  (TL, TR, BL, BR)

This ensures:
  Cut TL → Front=1, Back=2 ✅
  Cut TR → Front=3, Back=4 ✅
  Cut BL → Front=5, Back=6 ✅
  Cut BR → Front=7, Back=8 ✅

Usage:
  python micro_print_arranger.py input.pdf output.pdf [--flip short]
"""

import sys
import os
import math
import io
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas

def create_error_page(width, height):
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=(width, height))
    can.setFont("Helvetica-Bold", 40)
    can.drawCentredString(width / 2.0, height / 2.0, "ERROR")
    can.setFont("Helvetica", 20)
    can.drawCentredString(width / 2.0, (height / 2.0) - 40, "(Extra Padding Page)")
    can.save()
    packet.seek(0)
    new_pdf = PdfReader(packet)
    return new_pdf.pages[0]


def get_page_order_long_edge(group_pages):
    """
    Long-edge flip (default duplex for portrait).
    Paper flips like a book: left ↔ right mirror.
    
    Front TL ↔ Back TR
    Front TR ↔ Back TL
    Front BL ↔ Back BR
    Front BR ↔ Back BL
    
    We want after cutting:
      TL cut: front=p1, back=p2
      TR cut: front=p3, back=p4
      BL cut: front=p5, back=p6
      BR cut: front=p7, back=p8
    
    Front page (TL, TR, BL, BR): p1, p3, p5, p7
    Back page  (TL, TR, BL, BR): p4, p2, p8, p6
    
    Because:
      Back TR (behind Front TL) = p2 → so Back TR = p2
      Back TL (behind Front TR) = p4 → so Back TL = p4
      Back BR (behind Front BL) = p6 → so Back BR = p6
      Back BL (behind Front BR) = p8 → so Back BL = p8
    """
    p1, p2, p3, p4, p5, p6, p7, p8 = group_pages
    front = [p1, p3, p5, p7]  # TL, TR, BL, BR
    back  = [p4, p2, p8, p6]  # TL, TR, BL, BR
    return front, back


def get_page_order_short_edge(group_pages):
    """
    Short-edge flip (notepad style).
    Paper flips top ↔ bottom.
    
    Front TL ↔ Back BL
    Front TR ↔ Back BR
    Front BL ↔ Back TL
    Front BR ↔ Back TR
    
    We want after cutting:
      TL cut: front=p1, back=p2
      TR cut: front=p3, back=p4
      BL cut: front=p5, back=p6
      BR cut: front=p7, back=p8
    
    Front page (TL, TR, BL, BR): p1, p3, p5, p7
    Back page  (TL, TR, BL, BR): p6, p8, p2, p4
    
    Because:
      Back BL (behind Front TL) = p2 → so Back BL = p2
      Back BR (behind Front TR) = p4 → so Back BR = p4
      Back TL (behind Front BL) = p6 → so Back TL = p6
      Back TR (behind Front BR) = p8 → so Back TR = p8
    """
    p1, p2, p3, p4, p5, p6, p7, p8 = group_pages
    front = [p1, p3, p5, p7]  # TL, TR, BL, BR
    back  = [p6, p8, p2, p4]  # TL, TR, BL, BR
    return front, back


def arrange_for_microprint(input_pdf_path, output_pdf_path, flip_type="long"):
    """
    Main function: reads input PDF, arranges pages for micro-print duplex printing.
    
    Args:
        input_pdf_path: Path to original PDF
        output_pdf_path: Path for rearranged output PDF
        flip_type: "long" for long-edge flip, "short" for short-edge flip
    """
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()
    
    total_pages = len(reader.pages)
    
    # Pad to multiple of 8 (blank pages add honge end mein)
    pages_needed = math.ceil(total_pages / 8) * 8
    
    print(f"📄 Input PDF: {input_pdf_path}")
    print(f"📊 Total pages: {total_pages}")
    print(f"📐 Pages after padding (multiple of 8): {pages_needed}")
    print(f"🔄 Flip type: {'Long Edge (Book style)' if flip_type == 'long' else 'Short Edge (Notepad style)'}")
    print(f"📑 Sheets needed: {pages_needed // 8}")
    print()
    
    # Choose order function
    order_func = get_page_order_long_edge if flip_type == "long" else get_page_order_short_edge
    
    # Process in groups of 8
    num_sheets = pages_needed // 8
    
    for sheet_num in range(num_sheets):
        start_idx = sheet_num * 8
        
        # Get 8 page indices (0-based), using None for blank pages
        group_indices = []
        for i in range(8):
            page_idx = start_idx + i
            if page_idx < total_pages:
                group_indices.append(page_idx)
            else:
                group_indices.append(None)  # Blank page
        
        # Get front and back order
        front_order, back_order = order_func(group_indices)
        
        # Display info
        sheet_label = f"Sheet {sheet_num + 1}"
        front_display = [f"P{idx+1}" if idx is not None else "BLANK" for idx in front_order]
        back_display = [f"P{idx+1}" if idx is not None else "BLANK" for idx in back_order]
        
        print(f"{'='*50}")
        print(f"📋 {sheet_label}")
        print(f"  FRONT (TL, TR, BL, BR): {', '.join(front_display)}")
        print(f"  BACK  (TL, TR, BL, BR): {', '.join(back_display)}")
        print(f"  ✂️  Cut Results:")
        
        # Show what each cut produces
        positions = ["TL", "TR", "BL", "BR"]
        for pos_idx, pos in enumerate(positions):
            f_idx = front_order[pos_idx]
            # Find corresponding back position
            if flip_type == "long":
                # TL↔TR, BL↔BR
                back_pos_idx = pos_idx ^ 1  # XOR with 1: 0↔1, 2↔3
            else:
                # TL↔BL, TR↔BR
                back_pos_idx = pos_idx ^ 2  # XOR with 2: 0↔2, 1↔3
            b_idx = back_order[back_pos_idx]
            
            f_label = f"P{f_idx+1}" if f_idx is not None else "BLANK"
            b_label = f"P{b_idx+1}" if b_idx is not None else "BLANK"
            print(f"    {pos}: Front={f_label}, Back={b_label}")
        print()
        
        # Add front page
        for idx in front_order:
            if idx is not None:
                writer.add_page(reader.pages[idx])
            else:
                width = float(reader.pages[0].mediabox.width)
                height = float(reader.pages[0].mediabox.height)
                writer.add_page(create_error_page(width, height))
        
        # Add back page
        for idx in back_order:
            if idx is not None:
                writer.add_page(reader.pages[idx])
            else:
                width = float(reader.pages[0].mediabox.width)
                height = float(reader.pages[0].mediabox.height)
                writer.add_page(create_error_page(width, height))
    
    # Write output
    with open(output_pdf_path, "wb") as f:
        writer.write(f)
    
    print(f"{'='*50}")
    print(f"✅ Output saved to: {output_pdf_path}")
    print(f"📝 Total pages in output PDF: {len(writer.pages)}")
    print()
    print(f"🖨️  PRINTING INSTRUCTIONS:")
    print(f"   1. Open {os.path.basename(output_pdf_path)} in your PDF viewer")
    print(f"   2. Print → Select 'Multiple pages per sheet' / 'Micro' / '4-up'")
    print(f"   3. Layout: 2x2 (2 columns, 2 rows)")
    print(f"   4. Page order: Left to Right, Top to Bottom")
    print(f"   5. Duplex: ON ({'Long Edge' if flip_type == 'long' else 'Short Edge'})")
    print(f"   6. Print ALL pages")
    print(f"   7. Cut each sheet into 4 pieces")
    print(f"   8. Each piece will have correct front-back pages! 🎉")


def print_order_table(total_pages, flip_type="long"):
    """Just prints the page order table without creating a PDF."""
    pages_needed = math.ceil(total_pages / 8) * 8
    order_func = get_page_order_long_edge if flip_type == "long" else get_page_order_short_edge
    
    print(f"\n{'='*60}")
    print(f"  MICRO PRINT PAGE ORDER TABLE")
    print(f"  Total pages: {total_pages} (padded to {pages_needed})")
    print(f"  Flip: {'Long Edge' if flip_type == 'long' else 'Short Edge'}")
    print(f"{'='*60}\n")
    
    num_sheets = pages_needed // 8
    
    for sheet_num in range(num_sheets):
        start = sheet_num * 8
        group = []
        for i in range(8):
            p = start + i
            group.append(p if p < total_pages else None)
        
        front, back = order_func(group)
        
        f_disp = [str(i+1) if i is not None else "—" for i in front]
        b_disp = [str(i+1) if i is not None else "—" for i in back]
        
        print(f"  Sheet {sheet_num+1} of {num_sheets}:")
        print(f"  ┌─────────────────────────────────────┐")
        print(f"  │ FRONT    TL: {f_disp[0]:>3}    TR: {f_disp[1]:>3}       │")
        print(f"  │          BL: {f_disp[2]:>3}    BR: {f_disp[3]:>3}       │")
        print(f"  ├─────────────────────────────────────┤")
        print(f"  │ BACK     TL: {b_disp[0]:>3}    TR: {b_disp[1]:>3}       │")
        print(f"  │          BL: {b_disp[2]:>3}    BR: {b_disp[3]:>3}       │")
        print(f"  └─────────────────────────────────────┘")
        print()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("=" * 60)
        print("  MICRO PRINT PDF ARRANGER")
        print("=" * 60)
        print()
        print("Usage:")
        print("  python micro_print_arranger.py <input.pdf> [output.pdf] [--flip short|long]")
        print()
        print("Examples:")
        print("  python micro_print_arranger.py mybook.pdf")
        print("  python micro_print_arranger.py mybook.pdf arranged.pdf")
        print("  python micro_print_arranger.py mybook.pdf arranged.pdf --flip short")
        print()
        print("Options:")
        print("  --flip long   : Long-edge duplex flip (default, book-style)")
        print("  --flip short  : Short-edge duplex flip (notepad-style)")
        print()
        print("  --order-only N : Just show page order table for N pages (no PDF)")
        print()
        
        # Show example for 8 pages
        print("Example order for 8 pages (long-edge flip):")
        print_order_table(8, "long")
        
        sys.exit(0)
    
    # Parse arguments
    flip_type = "long"
    order_only = None
    
    args = sys.argv[1:]
    
    # Check for --flip
    if "--flip" in args:
        flip_idx = args.index("--flip")
        if flip_idx + 1 < len(args):
            flip_type = args[flip_idx + 1].lower()
            if flip_type not in ("long", "short"):
                print("❌ Error: --flip must be 'long' or 'short'")
                sys.exit(1)
            args = args[:flip_idx] + args[flip_idx+2:]
    
    # Check for --order-only
    if "--order-only" in args:
        oo_idx = args.index("--order-only")
        if oo_idx + 1 < len(args):
            order_only = int(args[oo_idx + 1])
            print_order_table(order_only, flip_type)
            sys.exit(0)
    
    # Get input/output paths
    input_path = args[0]
    
    if not os.path.exists(input_path):
        print(f"❌ Error: File not found: {input_path}")
        sys.exit(1)
    
    if len(args) > 1:
        output_path = args[1]
    else:
        base, ext = os.path.splitext(input_path)
        output_path = f"{base}_microprint{ext}"
    
    arrange_for_microprint(input_path, output_path, flip_type)
