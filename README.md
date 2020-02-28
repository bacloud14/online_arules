# online_arules
This is a security exercise and also a beneficial arules service on the web. Association rules can find hidden patterns in categorical data on a variety of use cases (bank bills, shopping list, ...). This is intended to be for personal use and not for heavy serving.
This should be a secure implementation of association rules learning serving web users
This is not secure yet, and therfore not for production as is anyhow now.
Next:
* Secure the file upload. It has already of file limit of 2MB, also secure file name, I am not sure this is enough. 
* Seure repeating uploads and requests, captcha ? and it should have a global limit of uploads (on all clients in one time: like no more than 10 files uploaded on the globe).
* Secure the processing. It is secured against the long running processing. I am not sure this is enough though. The app generally must further limit its execution load (no more than 10 processing at a time for example) 
* More robust tabular file reading, probably let the user choose columns to be processed on client side before or after upload. Also more robust against formats, delimiters, ... (now it dumply expects a csv with delimiter=';'). 
* Pretty print results (rules)
* Probably serve by a beautiful (but sober?) rendering engine.
* Customize parameters on client side (should let the user experience min_support and min_confidence at a reasonable amounts.
* Session by file analysis. There is no session implementation yet. So a user could normally re-run processing on the same file with different parameters for say 5 times with one only upload.
* Write a script to delete back-up uploaded file securily from disk after the session is dead.
