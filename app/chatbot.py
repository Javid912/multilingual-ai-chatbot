from transformers import pipeline, AutoModelForSeq2SeqLM, AutoTokenizer
import torch
import sys

# Initialize models for different languages
models = {
    'multilingual': 'facebook/mbart-large-50-many-to-many-mmt',
    'dialog': 'facebook/opt-350m'  # Changed to a better text generation model
}

class MultilingualChatbot:
    def __init__(self):
        print("Initializing chatbot...")
        print(f"Loading translation model: {models['multilingual']}")
        # Load the multilingual translation model
        self.translator = AutoModelForSeq2SeqLM.from_pretrained(models['multilingual'], device_map='auto')
        self.translator_tokenizer = AutoTokenizer.from_pretrained(models['multilingual'])
        print("Translation model loaded successfully!")
        
        print(f"\nLoading conversation model: {models['dialog']}")
        # Load the conversation model
        self.conversation = pipeline('text-generation', model=models['dialog'], device_map='auto')
        print("Conversation model loaded successfully!")
        print("\nChatbot initialization complete!")
        
        sys.stdout.flush()
    
    def detect_language(self, text):
        # Simple language detection based on character sets
        if any('\u0600' <= char <= '\u06FF' for char in text):
            return 'fa'  # Farsi
        elif any('\u0590' <= char <= '\u05FF' for char in text):
            return 'de'  # German
        return 'en'  # Default to English
    
    def translate_to_english(self, text, source_lang):
        if source_lang == 'en':
            return text
            
        inputs = self.translator_tokenizer(text, return_tensors="pt")
        translated = self.translator.generate(
            **inputs,
            forced_bos_token_id=self.translator_tokenizer.lang_code_to_id['en_XX']
        )
        return self.translator_tokenizer.decode(translated[0], skip_special_tokens=True)
    
    def translate_from_english(self, text, target_lang):
        if target_lang == 'en':
            return text
            
        inputs = self.translator_tokenizer(text, return_tensors="pt")
        translated = self.translator.generate(
            **inputs,
            forced_bos_token_id=self.translator_tokenizer.lang_code_to_id[f'{target_lang}_XX']
        )
        return self.translator_tokenizer.decode(translated[0], skip_special_tokens=True)
    
    def get_response(self, message):
        # Detect input language
        source_lang = self.detect_language(message)
        
        # Translate to English if necessary
        english_message = self.translate_to_english(message, source_lang)
        
        # Get response in English
        response = self.conversation(english_message, 
                                   max_length=100,
                                   num_return_sequences=1,
                                   temperature=0.7,
                                   do_sample=True)[0]['generated_text']
        
        # Clean up the response (remove the input message from the generated text)
        response = response[len(english_message):].strip()
        
        # Translate response back to source language
        return self.translate_from_english(response, source_lang)

# Initialize the chatbot
chatbot = MultilingualChatbot()

def get_response(message):
    return chatbot.get_response(message)
