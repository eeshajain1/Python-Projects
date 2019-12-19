#Eesha Jain
'''This program takes a sheet of students scores and prints out the top three studnets and their grades
as well as the grades of all the students in the class 
'''
#grade recieved: 100%


def main(): 
  file = open("HW3-input.txt", "r")  
  score_sheet = []
  student_scores = []
  
  for line in file:
      score_sheet.append(line.split(" "))
  

     
      for i in range(len(score_sheet)):
          A, B, C, D, F = 0, 0, 0, 0, 0
          for j in range(len(score_sheet[0])):
          
              
             
              
              if(eval(score_sheet[i][j]) > 100):
                  ID = score_sheet[i][j]
              elif(eval(score_sheet[i][j]) >= 90 and eval(score_sheet[i][j]) <= 100):
                  A+=1 
              elif(eval(score_sheet[i][j]) >= 80 and eval(score_sheet[i][j]) < 90):
                  B+=1
              elif(eval(score_sheet[i][j]) >= 70 and eval(score_sheet[i][j]) < 80):
                  C+=1
              elif(eval(score_sheet[i][j]) >= 60 and eval(score_sheet[i][j]) < 70):
                  D+=1
              else: 
                  F+=1
              
      print('ID', ID, ':')
      print('Numbers of (A, B, C, D, F) are', '(', A, ',', B, ',', C, ',', D, ',', F, ')')
      
      if(B<= 9):
          B = str(0)+str(B)
      if(C<= 9):
          C = str(0)+str(C)
      if(D<= 9):
          D = str(0)+str(D)
      if(F<= 9):
          F = str(0)+str(F)
          
      grade_string = (str(A)+str(B)+str(C)+str(D)+str(F) + str(ID))
      grade_string = int(grade_string)
      student_scores.append(grade_string)
      student_scores.sort()
      student_scores.reverse()
  
      
  print() 
  print("The top three students are: ")
  #Explanation of for loop: grade_string can only have two length values: 18 or 17. If the length value is 18, then the first 10 numbers are printed out 
  #as the grade, and if not, then the first 9 values are printed out as the grade and the rest are printed out as the ID
  for i in range(3): 
      student_scores[i] = str(student_scores[i])
      if(len(student_scores[i]) == 18): 
          print("Grade: " + student_scores[i][0:10], "ID:", student_scores[i][10:])
      else:
          print("Grade: " + student_scores[i][0:9], "ID:", student_scores[i][9:])
          
main()
 
 
 
 
 
 
 
 