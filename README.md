This program is designed to transcribe audio files and  translate the transcripts to English. It utilizes Google Speech-to-Text for speech recognition and Google Translate for language conversion.

Features


Automatic language detection
Transcript generation in the detected language
Optional translation of transcripts to English
Basic noise reduction (spectral subtraction)
Installation

The program requires the following Python libraries:

speech_recognition
googletrans
langdetect
numpy
hmmlearn
argparse
os

You can install them using the pip package manager:


'''pip install speech_recognition googletrans langdetect numpy hmmlearn argparse os'''

Usage

The program can be executed from the command line. Here's a breakdown of the available options:

Required Arguments:

-f, --file: Path to a single audio file for transcription.
-d, --directory: Path to a directory containing audio files for transcription. (Recursive processing can be enabled with the -r option)
Optional Arguments:

-r, --recursive: Process audio files in subdirectories of the input directory. (Only applicable with -d)
-t, --translate: Translate transcripts to English after recognition.
-n, --noise_reduction: Apply basic noise reduction to audio before processing.

Example Usage:

Transcribe a single audio file and create a transcript file:

'''python audio_transcript_generator.py -f speech.mp3'''

Transcribe all audio files in a directory (recordings) and translate transcripts to English:

'''python audio_transcript_generator.py -d recordings -t'''

Process audio files recursively within a directory (audio_data) and apply noise reduction:

'''python audio_transcript_generator.py -d audio_data -r -n'''

Output

For each processed audio file, the program generates a transcript file named <filename>-transcript.txt in the same directory. If translation is enabled, an additional file named <filename>-transcript_en.txt is created containing the English translation.

Logging

The program uses Python's logging module to provide informative messages during execution. These messages are printed to the console by default (INFO level). You can adjust the logging level (e.g., DEBUG, WARNING) using the -v or --verbose option (not implemented yet).

Error Handling

The program attempts to handle various errors that might occur during processing, such as file not found, unsupported format, or speech recognition failures. In case of errors, informative messages are logged to the console.


