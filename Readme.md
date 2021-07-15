    sudo apt install python3-virtualenv    
    virtualenv charvalue_venv
    sudo chmod +x charvalue_venv/bin/activate
    source charvalue_venv/bin/activate

    pip3 freeze > requirements.txt
    pip3 install -r requirements.txt
    

For large json formatting

    cat ugly.json | python -mjson.tool > pretty.json

run mysql locally by:

    mysql -u admin -p
    password: admin@123

Feature Notes: Politicians
    
    title
    date of birth (P569)
    place of birth (P19)
    date of death (P570)
    occupation (P106)
    sex or gender (P21)
    Description:    position held (P39), 
                    member of political party (P102) ,
                    candidacy in election (P3602)
    Acheivement: award received (P166)