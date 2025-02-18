import PyPDF2 as pdf
import easygui as eg

# Keep the application running
while True:
    
    # Ask user for the input file
    input_file_path = eg.fileopenbox(
        msg="Choose a PDF to open"
    )
    if input_file_path is None:
        confirmation = eg.buttonbox(msg='Do you wish to exit the application?', choices=['Yes', 'No'])
        if confirmation=="Yes":
            break
        elif confirmation=='No':
            continue
    else:
        # Open the PDF file
        pdf_reader = pdf.PdfReader(input_file_path)
        if pdf_reader.numPages > 0:
            # Ask for the page to rotate
            page_number = eg.integerbox(
                msg="Choose a page to rotate",
                title="Rotate PDF Page",
                lowerbound=1,
                upperbound=pdf_reader.numPages
            )
            if page_number is not None:
                # Ask for the rotation angle
                rotation_angle = eg.integerbox(
                    msg="Enter the rotation angle in degrees",
                    title="Rotate PDF Page",
                    default=90
                )
                if rotation_angle is not None:
                    # Rotate the page and save the new PDF
                    output_file_path = eg.filesavebox(
                        msg="Save the rotated PDF",
                        default=f"{input_file_path[:-4]}_rotated_{rotation_angle}deg.pdf"
                    )
                    if output_file_path is not None:
                        with open(output_file_path, 'wb') as output_file:
                            pdf_writer = pdf.PdfWriter(output_file)
                            page = pdf_reader.pages[page_number - 1]
                            page.rotateClockwise(rotation_angle)
                            pdf_writer.addPage(page)
                            for i in range(pdf_reader.numPages):
                                if i != page_number - 1:
                                    pdf_writer.addPage(pdf_reader.pages[i])
                            pdf_writer.write(output_file)
                    else:
                        eg.msgbox(msg='Operation cancelled by user', title='Rotate PDF Page')
                else:
                    eg.msgbox(msg='Operation cancelled by user', title='Rotate PDF Page')
            else:
                eg.msgbox(msg='Operation cancelled by user', title='Rotate PDF Page')
        else:
            eg.msgbox(msg='The selected PDF file is empty', title='Rotate PDF Page')