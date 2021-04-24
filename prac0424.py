symbols = 'HPQ,AAPL,IBM,MSFT,YHOO,DOA,GOOG'
symlist = symbols.split(",")

# for s in symlist:
#   print("s=",s)

symlist.append('YHOO')
# print(symlist)

# print(symlist.index("YHOO"))

# print(symlist[4])
print(symlist.count("YHOO"))

symlist.remove("YHOO")

print(symlist)
symlist.sort()
print(symlist)
symlist.sort(reverse=True)
print(symlist)


