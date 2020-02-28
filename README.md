# online_arules
This should be a secure implementation of association rules learning serving web users
This is not secure yet, and therfore not for production as is anyhow now.
Next:
* Secure the file upload. It has already of file limit of 2MB, also secure file name, I am not sure this is enough. 
* Seure repeating uploads and requests, captcha ?
* Secure the processing. It is secured against the long running processing. I am not sure this is enough though.
* More robust tabular file reading, probably let the user choose columns to be processed on client side before or after upload. Also more robust against formats, delimiters, ... (now it dumply expects a csv with delimiter=';'). 
* Pretty print results (rules)
* Probably serve by a beautiful (but sober?) rendering engine.
* Customize parameters on client side (should let the user experience min_support and min_confidence at a reasonable amounts.
* Session by file analysis. There is no session implementation yet. So a user could normally re-run processing on the same file with different parameters for say 5 times with one only upload.
* Write a script to delete back-up uploaded file securily from disk after the session is dead.
