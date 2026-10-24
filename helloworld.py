#Q1
print('git init\n 
SSH -T git@github.com # to be sure of verification\n 
git remote add origin (repo link)\n
gh auth status #check status\n
gh auth login # if is needed\n
gh repo create lab6 --public')
#Q2
print('gh api --method PUT repo/Jose-L0-M4/lab6/collaborators/lomantilla2006')
#Q3                                     
print('tgh api repos/Jose-L0-M4/lab6/collaborators')
#Q4
print('gh api --method DELETE repos/Jose-L0-M4/lab6/collaborators/lomantilla2006
')
#Q5 
print('gh issue create   --title "create helloworld echo file"   --body "echo hello Pearse from lab6"   --assignee "@me"   --label "enhancement"')
