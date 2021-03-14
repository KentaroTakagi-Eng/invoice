class Extract():

    def __int__(self):
        Type(case="HK1", company_name = "text_list[7]", payment_amount = "(text_list[-1]).split()[-2:]")
        Type(case="MY1", company_name= "text_list[-1]", payment_amount="text_list[-3]")
        Type(case="MY2", company_name= "(text_list[0]).split()[:4]", payment_amount="text_list[-1]")
        Type(case="SG1", company_name= "(text_list[0]).split()[:2]", payment_amount="text_list[-1]")
        Type(case="SG2", company_name= "text_list[0]", payment_amount="(text_list[-1]).split()[-2:]")
        Type(case="SG3", company_name= "(text_list[0]).split()[:3]", payment_amount="text_list[-1]")
        Type(case="SG4", company_name= "(text_list[0]).split()[1:3]", payment_amount="(text_list[-1]).split()[-2]")
        Type(case="SG5", company_name= "(text_list[0]", payment_amount="(text_list[-1]).split()[-2:]")
        Type(case="TH1", company_name= "text_list[0]", payment_amount="text_list[-1]")
        Type(case="TW1", company_name= "text_list[0]", payment_amount="(text_list[-1]).split()[-2:]")
        Type(case="TW2", company_name= "(text_list[0]).split()[0:3]", payment_amount="text_list[-4]")
        Type(case="TW3", company_name= "text_list[2]", payment_amount="text_list[-1]")


