# Time Talker
A simple Python program that will read the time out loud.

Developed on a Debian system in January 2014. 

- Requires eSpeak, MBROLA
- Python and Jinja2

Subprocess calls espeak, a free TTS engine, with a time string.

The time string is created with Jinja2 and a template (template/time.ssml).
