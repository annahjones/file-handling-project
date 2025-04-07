def read_and_modify_file():
    try:
        # Ask the user to enter the input file name
        input_filename = input("Enter the name of the file to read from: ")

        # Try to open the input file
        with open(input_filename, 'r') as infile:
            content = infile.read()
            print("\n📄 Original File Content:")
            print(content)

            # Modify the content (Example: convert to uppercase)
            modified_content = content.upper()

            # Ask user for output file name
            output_filename = input("\nEnter the name of the file to save modified content: ")

            # Write modified content to new file
            with open(output_filename, 'w') as outfile:
                outfile.write(modified_content)

            print(f"\n✅ Modified content written successfully to '{output_filename}'.")

    except FileNotFoundError:
        print("\n❌ Error: File not found. Please check the filename and try again.")
    except IOError as e:
        print(f"\n❌ I/O error occurred: {e}")
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")

# Run the function
read_and_modify_file()
