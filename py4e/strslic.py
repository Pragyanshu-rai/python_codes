text= "X-DSPAM-Confidence:    0.8475"
p=text.find('0')
n=float(text[p:])
print(n)
