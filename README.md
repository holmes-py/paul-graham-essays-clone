# paul-graham-essays-clone
I wanted to read his essays on my kindle, there was no way to download the pdfs of 200+ essays, wrote this quick script to make pdfs of all of them and store in a folder called pdfs. You can then transfer them over to your kindle. This is using a library, and some multiprocessing to speed it up.   

Be aware of running it on low powered systems. Decrease the count in Pool() function to <4 to make it smoother. 
It should run normally if you have chrome installed anywhere on system, otherwise, refer to the library's documentation to figure out how to add custom chromedriver path. 


You will need to use:  
```python
pip install pyhtml2pdf
```
