print(""" ################################## REINFORCEMENT PLATE CALCULATIONS####################################
================================================ AWWA==================================Mech.Eng.HamiKESERCI

################ P Internal pressure as psi
################ D-MainPipe Outter Diameter as inc
################ d-Branch Outter Diameter as inc
################ Δ-Between MainPipe and Branch Degree as decimal

        #  --------------------------------------------------------  #
      #                       (P x d^2)                                #
     <                PDV= ------------                                 >
      #                       D x sinΔ                                 #
        #  --------------------------------------------------------  #   """)


P=float(input("Please enter the P : "))
D=float(input("Please enter the D : "))
d=float(input("Please enter the d : "))
Delta=float(input("Please enter the  Δ: "))
sinΔ={}
if Delta==90:
    sinΔ=1
elif Delta==60:
    sinΔ=float(0.86)
elif Delta==30:
    sinΔ=float(0.5)
else:
    print("Plase Calculate the sinΔ for the calculations")
PDV= int(P*d**2)/(D*sinΔ*sinΔ) 
print("""PDV: PDV is control for the which reinforcement plate that we use\n*****************************{}***********************""".format(PDV))
M1,M2=float(25*10**(-5)),int(1)
if PDV>6000:
    print("             ****USE CROTCH PLATE****")
    print("##########Contuniue the Crotch Calculatıons########")
    dp=int(input("Use the 13.7 graph for the  dp: "))
    t1=input("use the 13.7 graph for the  t1: ")
    try: 
        t=float(input("select new thickness of plate t: "))
        print("new thicknes",t)
    except:
        print("please enter the float with '.' ")
    a=float(Delta/360)
    b=float(0.917)
    x=b-a
    Nw=int(input("Use the 13.8 graph for the  Nw: "))
    Nb=int(input("Use the 13.8 graph for the  Nb: "))
    Qw=int(input("Use the 13.9 graph for the  Qw: "))
    Qb=int(input("Use the 13.9 graph for the  Qb: "))
    dw=Nw*dp
    db=Nb*dp
    dw2=Qw*dw
    db2=Qb*db
    print("dw:  {}\ndb: {}\ndw2: {}\ndb2: {} ".format(dw,db,dw2,db2))
    tmp=float(input("mainpipe thickness: "))
    tbp=float(input("branch thickness  : "))
    Pw,Pd=P,P*1.5
    radm=float(D/2)
    radm1=radm-tmp
    radb=float(d/2)
    radb1=float(radb-tbp)
    Rmp,Rbp=radm1,radb1
    print("main pipe inside radius:  {}\nbranch pipe radius: {}".format(Rmp,Rbp))
    #dts=float(0)
    dts=float(input("for single crotch 13.10 graph d\'t dts:"))
    #dpt=float(0)
    dpt=float(input("depth of plate for two crotch 13.10 graph dt dpt:"))
    dwrt= int(dw*((int(t1)/int(t))**x))
    dbrt= int(db*((int(t1)/int(t))**x))
    dwrs= (dw2*((int(t1)/int(t))**x))
    dbrs= (db2*((int(t1)/int(t))**x))
    print("new depth of the plate d1=dw: {}\nnew depth of the plate d1=db: {}\nnew depth of the plate as d\'w d1=dw2: {}\nnew depth of the plate as d\'b d1=db2:  {}".format(dwrt,dbrt,dwrs,dbrs))
    if Rmp==Rbp:
       dts==(dts+Rmp) 
       dpt==(dpt+Rbp) 
       print(dts)
       print(dpt)
    print(" USE THE VALUE OF SINGULAR CROTCH PLATE")
    print("dwrs: ",int(dwrs),"dbrs: ",int(dbrs),"dts: ",int(dts))
    print("USE THE VALUE OF TWO CROTCH PLATE")
    print("dwrt: ",int(dwrt),"dbrt: ",int(dbrt),"dpt :",int(dpt))
    print("*******CALCULATIONS FINISHED********")
elif 4000<PDV<6000 and d/D>float(0,7):
    M=M1
    print("Use Wrapper Plate")
elif PDV<4000 and d/D>float(0,7):
    M=M2
    print("Use Wrapper Plate")
elif 4000<PDV<6000 and d/D<=float(0,7):
    M=M1
    print("Use Collar Plate")
elif PDV<4000 and d/D<=float(0,7):
    M=M2
    print("Use Wrapper Plate")
 
 
# Hocam programı çalıştırdığınızda input değerleri sırasıyla bu değerleri girmenz gerekıyor : 870-30-30-90-32-1-1.2-1-1-1-1-0.94-0.94-19.5-14