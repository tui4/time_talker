# Time Talker
A simple program that will read the time out loud.

- Requires espeak, mbrola 
- Python and Jinja2

Subprocess calls espeak, a free TTS engine, with a time string.
The time string is created with Jinja2 and a template (template/time.ssml).