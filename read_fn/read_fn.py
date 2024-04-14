import os

def main():

    directory = r'C:\Users\admin\Desktop\book\ai'


    if not os.path.exists(directory):
        print(f" '{directory}' not exist.")
        return

    
    files = os.listdir(directory)


    pdf_files = [file for file in files if file.endswith('.pdf')]

    
    if pdf_files:
        print(" PDF :")
        for pdf_file in pdf_files:
            print(pdf_file)
    else:
        print("not found .")

if __name__ == "__main__":
    main()
