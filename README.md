# T2T_Translator-Assamese--Nalbaria-

The Assamese language, primarily spoken in the state of Assam, exhibits variations in vocabulary, intonation, and pronunciation across different regions. Dialectical differences are prominent, with various Assamese dialects prevailing in different areas. For instance, the Central Assam region, including Nagaon and nearby areas, has a distinct dialect compared to Eastern Assam. The Kamrupi dialect is widespread in regions such as Kamrup, Nalbari, Barpeta, Goalpara, Bongaigaon, with variations like Nalbaria, Barpetia, Goalparia spoken in respective districts. Communication challenges arise as people may struggle to understand each other's dialects, particularly in remote villages where some may not be familiar with standard Assamese.

To address this communication gap, there is a need for a system that facilitates effective information exchange among the indigenous people, regardless of their dialects. With technological advancements, various translators and speech synthesis systems have emerged worldwide. In Assam, a system is required to convert speech between standard Assamese and different dialects. The focus of this project is to design and implement a text-to-speech (TTS) system specifically for the Nalbaria variety of Assamese. Due to resource constraints, **the initial step involves creating a text-to-text (T2T) translator module for translating text from the standard variety to Nalbaria.** This system aims to benefit the indigenous people, particularly the Nalbaria society, promoting effective communication and understanding among diverse dialects within Assam.

# Layout and Operation of the Translator:

**Input:**
The translator processes transliterations of standard Assamese, utilizing a set of phonemes. For instance, 'Ki kaxri aasaa?' is transformed into the question 'What are you doing?'

**Tokenization:**
Following the input, the system breaks down the sentence into individual tokens, such as 'Ki,' 'Kaxri,' and 'aasaa.'

**Stemming and Syllabification Rules:**
In the stemming phase, the system identifies root words by referencing a pre-built dictionary. This mapping aids in recognizing suitable Nalbaria equivalents. The obtained suffix after stemming provides details like the addressee and prosody. For words not in the root word list or those unmatched with given suffixes, syllabification rules come into play. These rules, developed through observation, guide the conversion of new words to Nalbaria by either introducing a suffix or altering the position of a vowel in the standard word.

![image](https://github.com/Garg998/T2T_Translator-Assamese--Nalbaria-/assets/151191852/276ab61d-6848-41a6-92a1-37cbec727e30)

![image](https://github.com/Garg998/T2T_Translator-Assamese--Nalbaria-/assets/151191852/d523c736-7f5b-4187-81d9-cc794322a825)

