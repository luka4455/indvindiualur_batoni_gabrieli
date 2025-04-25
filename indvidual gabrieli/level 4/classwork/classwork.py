#1) შექმენი 5 ლოგიკური ოპერაციის მაგალითი   
#2)შექმენი 5 შედარების ოპერაციის მაგალითი
#3) ახსენი როგორ მუშაობს and და or ოპერეტორები
#4) გააერთიანე ლოგიკური და შედარების ოპერაციები და შექმენი 5 მაგალითი (თითოეულ მაგალითში შედეგი მიუქერე რას გამოიტანს კომენტარით)
#5) შემქენი ორი ცვლადი რომელშიც შეინახავ შედარების ოპერატორს როგორც შედეგს და მასზე მათზე მოახდინე ლოგიკური ოპერაციები.

#1 
print(True or False)#True
print(True, True, True and False)#False
print(False, False, False or True, False)#True
print(True, True and False)#False
print(True and False)#False


#2
number = 759
number2 = 849
number3 = 95
number4 = 83
number5 = 84

print(number < number2 or number3 < number4)
print(number2 > number3 and number4 > number5)




#3
print(True or False)#ორ მაგალითად რომ დავწეროთ ბევრი ფალსი და ერთი ორ თრუ გამოიტანს თრუს
print(True and False)#ენდ მაგალითად რომ ეწეროს ბევრი თრუ და ერთი  ენდ ფალსი  გამოიტანს ფალს


#4
num = 23
num2 = 938
num3 = 49
num4 = 38
num5 = 94

print((num > num2) or False)#False
print((num3 > num4) or False)#True
print((num4 > num5) and True)#False


#5
numberr = 15 < 9
numberr2 = 11 < 29

print(numberr)
print(numberr2)
