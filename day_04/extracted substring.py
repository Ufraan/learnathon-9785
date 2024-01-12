sentence = input("Enter a sentence: ")

if len(sentence) >= 10:
    extracted_substring = sentence[4:10]  
    print("Extracted Substring:", extracted_substring)
else:
    print("Input sentence should have at least 10 characters.")