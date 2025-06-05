'''Consists of functions to remove noise from our text'''



noise = ['am','this',',','.','the','are','is','since','at','and','a'] #list containing noisy words as per our requirement

def remove_noise(input_text):

    words = input_text.split(" ")
    noise_free_words = [word for word in words if word not in noise]
    no_noise_text = " ".join(noise_free_words)

    return no_noise_text

print("\n")
text = "this is a very wholesome morning since I woke up early and am at work now ."
print(f"Input Text: {text}\nText after removing noise:  {remove_noise(text)}")


#removing regex expression
import re
def remove_regex(input_text,regex_pattern):

    urls = re.finditer(regex_pattern, input_text) 
    for i in urls: 
        input_text = re.sub(i.group().strip(), '', input_text)

    return input_text

print("\n")
regex_pattern = "#[\w]*"
text = "this is a very wholesome #mindful morning since I woke up #early and am at work now and can make money ."
print(f"Input Text: {text}\nText after removing noise:  {remove_regex(text, regex_pattern)}")