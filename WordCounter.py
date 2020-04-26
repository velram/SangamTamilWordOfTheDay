from collections import Counter 
  
def count_words_fast(text):      #counts word frequency using Counter from collections 
    text = text.lower() 
    skips = [".", ", ", ":", ";", "'", '"'] 
    for ch in skips: 
        text = text.replace(ch, "") 
    word_counts = Counter(text.split(" ")) 
    return word_counts 
  
text = "செங்களம் படக்கொன் றவுணர்த் தேய்த்த செங்கோ லம்பிற் செங்கோட்டி யானைக் கழல்தொடிச் சேஎய் குன்றம் குருதிப் பூவின் குலைக்காந் தட்டே செங்களம் படக்கொன் றவுணர்த் தேய்த்த செங்கோ லம்பிற் செங்கோட்டி யானைக் கழல்தொடிச் சேஎய் குன்றம் குருதிப் பூவின் குலைக்காந் தட்டே"  
print(count_words_fast(text))