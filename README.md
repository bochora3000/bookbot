# Text Analysis Report Generator 📚

This project is a simple Python program that reads the content of a text file and generates a comprehensive report, including word count and character frequency. The current implementation uses Mary Shelley's *Frankenstein* as the sample text.

## Features

- **Word Count**: Calculates the total number of words in the document.
- **Character Frequency Analysis**: Counts the occurrences of each character in the document (case-insensitive).
- **Readable Report**: Outputs a clean and structured summary of the analysis.

## How It Works

1. The program reads the content of a text file (`books/frankenstein.txt`).
2. It calculates:
   - The total word count.
   - The frequency of each character (letters, punctuation, whitespace, etc.).
3. Outputs the results in a structured format to the console.

### Example Output
```
--- Begin report of books/frankenstein.txt ---
75324 words found in the document

The 't' character was found 56078 times
The 'h' character was found 32453 times
The 'e' character was found 89012 times
...
--- End report ---
```

## File Structure

```
.
├── books/
│   └── frankenstein.txt   # Sample text file for analysis
└── main.py                # Main script with word and character analysis logic
```

## Code Breakdown

### Main Function
The `main()` function coordinates the program:
- Reads the text file.
- Calls helper functions for word count and character frequency analysis.
- Prints the analysis results in a readable format.

### Helper Functions
- **`word_counter(book_as_a_string)`**: Splits the input text into a list of words and returns the word count.
- **`character_counter(book_as_a_string)`**: Counts occurrences of each character in the text (case-insensitive) and returns a dictionary of character counts.

## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/text-analysis-report-generator.git
   ```
2. Navigate to the project directory:
   ```bash
   cd text-analysis-report-generator
   ```
3. Ensure `frankenstein.txt` is in the `books` folder.
4. Run the script:
   ```bash
   python main.py
   ```

## Customization
You can analyze any `.txt` file by:
1. Placing your file in the `books` directory.
2. Changing the file path in the `main()` function:
   ```python
   with open("books/your_file.txt") as book:
   ```

## Future Enhancements

- Exclude punctuation and whitespace from character frequency analysis.
- Provide an option to analyze multiple files.
- Add a graphical user interface (GUI).
- Save the report to a separate output file.

## Contributing

Feel free to fork this repository and submit pull requests for improvements or new features.

## License

This project is open-source and available under the [MIT License](LICENSE).
