SKILL_BUCKETS = {
    "programming_languages": [
        {"java", "Core Java", "Java Enterprise Edition", "JavaSE"},
        {"kotlin", "elixir"},
        {"xml", "JSP"},
        {"swift", "Swift (Programming Language)"},
        {"android", "android jetpack", "android data binding", "Android Development", "Android Studio"},
        {"ios", "ios development"},
        {"r", "R Programming"},
        {"python", "Python (Programming Language)"},
        {"php"},
        {"javascript", "js", "JavaScript eXtension (JSX)", "Three.js", "typescript"},
        {"HTML", "HTML5", "HTML 5"},
        {"CSS", "Cascading Style Sheets (CSS)", "sass", "less", "Tailwind CSS", "scss", "CSS Flexbox"},
        {"golang", "Go (Programming Language)"},
        {"c++"},
        {"c#"},
        {"c", "C (Programming Language)"},
        {"ruby", "ruby or rails"},  # 13
        {"perl", "Perl Script"},
        {"Shell Scripting", "Bash"},
        {"Scala", "Scala (Programming Language)"},
    ],
    "backend_frameworks": [
        {"Back-End Web Development"},
        {"ASP.NET", "ASP.NET Core", "ASP.NET MVC", ".NET", ".NET Framework", ".NET Core", "Asp.net identity",
         "asp.net core Web API", "ASP.NET WEB API", "LINQ", "Entity Framework", "WCF", "blazor"},
        {"django"},
        {"spring", "Spring Framework", "Spring MVC", "Spring Boot"},
        {"laravel"},
        {"Node.js", "Node", "Node js"},
        {"Express.js", "Express"},
    ],
    "devops_technologies": [
        {"kubernetes", "helm chart", "Helm Charts", "openshift", "prometheus"},
        {"docker", "Docker Products"},
        {"ansible"},
        {"infrastructure"},  # 3
        {"google cloud platform", "Google Cloud Platform (GCP)"},
        {"azure", "Azure DevOps", "Microsoft Azure", "Microsoft Azure task management"},
        {"containerization", "Virtualization"},
        {"aws", "amazon web services certified solutions architect", "Amazon CloudFront", "AWS Lambda",
         "Amazon Redshift", "Amazon Web Services (AWS)", "AWS CloudFormation", "Amazon ECS"},
        {"jenkins"},
        {"CI-CD", " Continuous Delivery", "Continuous Integration", "Continuous Improvement"},
        {"cloud endure", "cloud migration", "cloud backup", "cloud computing"},
        {"devops"},
    ],
    "frontend_frameworks": [
        {"react", "React.js", "react hook", "react js", "React Native", "nextjs"},
        {"vuejs", "vue.js"},
        {"angular", "angularjs", "Angular Material", "Angular 6"},
        {"redux", "Redux.js", "Redux Thunk"},
        {"ajax"},
        {"jquery"},
        {"bootstrap"},
    ],
    "system_design_skills": [
        {"mobile application", "mobile applications"},
        {"oop", "Object-Oriented Programming (OOP)", "Object Oriented Design"},
        {"design patterns", "software design patterns", "Software Design"},
        {"Systems Engineering", "Distributed Systems", "software engineering"},
        {"programming"},
        {"algorithm", "algorithms", "Data Structures and algorithms", "data structures", "Graph Theory"},
        {"web development", "grpc"},
        {"web applications", "Web Application Firewall", "Web Services", "Web Application Security",
         "web application penetration testing"},
        {"microservices"},
        {"Software Testing", "Test Driven Development", "Test Automation", "unit testing"},
        {"Unified Modeling Language (UML)", "uml"},
    ],
    "version_controls": [
        {"git", "gitflow", "Gitlab", "Github"},
    ],
    "ui-ux": [
        {"graphic design", "Computer Graphics"},
        {"illustrator"},
        {"figma", "adobe xd", "Google Material Design"},
        {"photoshop", "adobe photoshop"},
        {"ui-ux", "User Interface Design", "User Experience (UX)", "Ui Designer", "Ux design",
         "User Interface Prototyping", "Material-UI"},
    ],
    "data_related": [
        {"data integration"},
        {"big data", "Big Data Analytics", "Data Engineering"},
        {"data"},
        {"spark", "Apache Spark", "PySpark"},
        {"Information Retrieval"},
        {"Data Visualization"},
        {"Selenium"},
        {"PySpark"},
        {"mapreduce"},
        {"Zeppelin"},
        {"Hadoop"},
        {"Apache Sqoop", "sqoop"},
        {"Tableau"},
        {"hdfs"},
        {"Apache Oozie", "Oozie"},
        {"Data Warehousing"},
        {"Apache Ambari"},
        {"Cloudera Impala", "Apache Impala", "Impala"},
        {"Snowflake"},
    ],
    "databases": [
        {"data migration"},
        {"mongodb"},
        {"database design"},
        {"nosql"},
        {"mysql"},
        {"postgresql"},
        {"sqlite"},
        {"graphql"},
        {"elasticsearch", "Elastic Stack (ELK)"},
        {"redis"},
        {"data center"},
        {"mariadb"},
        {"oracle"},
        {"SQLite"},
        {"sql", "Microsoft SQL Server", "SQL Server Management Studio", "PL/SQL", "T-SQL", "Transact-SQL (T-SQL)",
         "SSRS"},
    ],
    "ai_modeling": [
        {"Artificial Intelligence (AI)", "AI", "Artificial Intelligence"},
        {"regression testing"},
        {"predictive modeling"},
        {"Machine Learning", "Machine Learning Algorithms"},
        {"image processing"},
        {"data science"},
        {"NLP", "Natural Language Processing (NLP)"},
        {"data modeling"},
        {"computer vision"},
        {"big data"},
        {"deep learning"},
        {"data mining"},
        {"Data Analysis"},
        {"MLOps"},
        {"Supervised Learning", "Unsupervised Learning"},
        {"Recommender Systems"},
        {"Data Preprocessing"},
    ],
    "ai_frameworks": [
        {"pandas", "Pandas (Software)"},
        {"pytorch"},
        {"keras"},
        {"tensorflow"},
        {"scikit-learn"},
        {"seaborn"},
    ],
    "network_skills": [
        {"Dynamic Host Configuration Protocol (DHCP)"},
        {"Domain Name System (DNS)"},
        {"routing protocols", "Routing"},
        {"Routers"},
        {"cisco"},
        {"wireless"},
        {"vpn", "SSLVPN"},
        {"switching"},
        {"dhcp server"},
        {"network security"},
        {"lan-wan"},
        {"hacking"},
        {"cybersecurity"},
        {"penetration test", "Penetration Testing"},
        {"network administration", "Server Administration", "Networking", "Computer Networking"},
        {"network security"},
        {"ip"},
        {"TCP/IP"},
    ],
    "message_brokers": [
        {"apache kafka"},
        {"rabbitmq"},
    ],
    "hardware_skills": [
        {"FPGA", "Field-Programmable Gate Arrays (FPGA)"},
        {"PCB design", "Printed Circuit Board (PCB)"},
        {"VLSI", "Very-Large-Scale Integration (VLSI)"},
        {"IOT"},
        {"circuit design", "Electronic Circuit Design"},
        {"embedded"},
        {"Computer Architecture"},
        {"PSpice"},
        {"microcontroller"},
        {"Controller Area Network (CAN)"},
        {"signal processing"},
        {"raspberry pi"},
        {"verilog"},
        {"stm32"},
        {"ARM", "ARM Assembly"},
        {"xilinx"},
        {"arduino"},
        {"simulink"},
        {"matlab"},
        {"VHDL"},
        {"proteus"},
    ],
    "os": [
        {"linux", "Red Hat Linux", "Linux Kernel", "Arch Linux", "Kali Linux", "CentOS"},
        {"vmware", "VMware Infrastructure"},
        {"Windows Server", "Windows"},
    ]
}


def init_skill_counts():
    counted_skills = {
        "programming_languages": [False for i in range(len(SKILL_BUCKETS["programming_languages"]))],
        "backend_frameworks": [False for i in range(len(SKILL_BUCKETS["backend_frameworks"]))],
        "devops_technologies": [False for i in range(len(SKILL_BUCKETS["devops_technologies"]))],
        "frontend_frameworks": [False for i in range(len(SKILL_BUCKETS["frontend_frameworks"]))],
        "system_design_skills": [False for i in range(len(SKILL_BUCKETS["system_design_skills"]))],
        "version_controls": [False for i in range(len(SKILL_BUCKETS["version_controls"]))],
        "ui-ux": [False for i in range(len(SKILL_BUCKETS["ui-ux"]))],
        "data_related": [False for i in range(len(SKILL_BUCKETS["data_related"]))],
        "databases": [False for i in range(len(SKILL_BUCKETS["databases"]))],
        "ai_modeling": [False for i in range(len(SKILL_BUCKETS["ai_modeling"]))],
        "ai_frameworks": [False for i in range(len(SKILL_BUCKETS["ai_frameworks"]))],
        "network_skills": [False for i in range(len(SKILL_BUCKETS["network_skills"]))],
        "message_brokers": [False for i in range(len(SKILL_BUCKETS["message_brokers"]))],
        "hardware_skills": [False for i in range(len(SKILL_BUCKETS["hardware_skills"]))],
        "os": [False for i in range(len(SKILL_BUCKETS["os"]))],
    }

    return counted_skills


def skills_to_lowercase():
    SKILL_PROGRAMMING_LANGUAGE = []
    SKILL_BACKEND_FRAMEWORKS = []
    SKILL_DEVOPS_TECHNOLOGIES = []
    SKILL_FRONTEND_FRAMEWORKS = []
    SKILL_SYSTEM_DESIGN = []
    SKILL_VERSION_CONTROL = []
    SKILL_UI_UX = []
    SKILL_DATA_RELATED = []
    SKILL_DATABASES = []
    SKILL_AI_MODELING = []
    SKILL_AI_FRAMEWORKS = []
    SKILL_NETWORK = []
    SKILL_MESSAGE_BROKERS = []
    SKILL_HARDWARE= []
    SKILL_OS = []

    for i in range(len(SKILL_BUCKETS["programming_languages"])):
        skill_set = set()
        for j in SKILL_BUCKETS["programming_languages"][i]:
            skill_set.add(j.lower())
        SKILL_PROGRAMMING_LANGUAGE.append(skill_set)

    for i in range(len(SKILL_BUCKETS["backend_frameworks"])):
        skill_set = set()
        for j in SKILL_BUCKETS["backend_frameworks"][i]:
            skill_set.add(j.lower())
        SKILL_BACKEND_FRAMEWORKS.append(skill_set)

    for i in range(len(SKILL_BUCKETS["devops_technologies"])):
        skill_set = set()
        for j in SKILL_BUCKETS["devops_technologies"][i]:
            skill_set.add(j.lower())
        SKILL_DEVOPS_TECHNOLOGIES.append(skill_set)

    for i in range(len(SKILL_BUCKETS["frontend_frameworks"])):
        skill_set = set()
        for j in SKILL_BUCKETS["frontend_frameworks"][i]:
            skill_set.add(j.lower())
        SKILL_FRONTEND_FRAMEWORKS.append(skill_set)

    for i in range(len(SKILL_BUCKETS["system_design_skills"])):
        skill_set = set()
        for j in SKILL_BUCKETS["system_design_skills"][i]:
            skill_set.add(j.lower())
        SKILL_SYSTEM_DESIGN.append(skill_set)

    for i in range(len(SKILL_BUCKETS["version_controls"])):
        skill_set = set()
        for j in SKILL_BUCKETS["version_controls"][i]:
            skill_set.add(j.lower())
        SKILL_VERSION_CONTROL.append(skill_set)

    for i in range(len(SKILL_BUCKETS["ui-ux"])):
        skill_set = set()
        for j in SKILL_BUCKETS["ui-ux"][i]:
            skill_set.add(j.lower())
        SKILL_UI_UX.append(skill_set)

    for i in range(len(SKILL_BUCKETS["data_related"])):
        skill_set = set()
        for j in SKILL_BUCKETS["data_related"][i]:
            skill_set.add(j.lower())
        SKILL_DATA_RELATED.append(skill_set)

    for i in range(len(SKILL_BUCKETS["databases"])):
        skill_set = set()
        for j in SKILL_BUCKETS["databases"][i]:
            skill_set.add(j.lower())
        SKILL_DATABASES.append(skill_set)

    for i in range(len(SKILL_BUCKETS["ai_modeling"])):
        skill_set = set()
        for j in SKILL_BUCKETS["ai_modeling"][i]:
            skill_set.add(j.lower())
        SKILL_AI_MODELING.append(skill_set)

    for i in range(len(SKILL_BUCKETS["ai_frameworks"])):
        skill_set = set()
        for j in SKILL_BUCKETS["ai_frameworks"][i]:
            skill_set.add(j.lower())
        SKILL_AI_FRAMEWORKS.append(skill_set)

    for i in range(len(SKILL_BUCKETS["network_skills"])):
        skill_set = set()
        for j in SKILL_BUCKETS["network_skills"][i]:
            skill_set.add(j.lower())
        SKILL_NETWORK.append(skill_set)

    for i in range(len(SKILL_BUCKETS["message_brokers"])):
        skill_set = set()
        for j in SKILL_BUCKETS["message_brokers"][i]:
            skill_set.add(j.lower())
        SKILL_MESSAGE_BROKERS.append(skill_set)

    for i in range(len(SKILL_BUCKETS["hardware_skills"])):
        skill_set = set()
        for j in SKILL_BUCKETS["hardware_skills"][i]:
            skill_set.add(j.lower())
        SKILL_HARDWARE.append(skill_set)

    for i in range(len(SKILL_BUCKETS["os"])):
        skill_set = set()
        for j in SKILL_BUCKETS["os"][i]:
            skill_set.add(j.lower())
        SKILL_OS.append(skill_set)

    SKILL_BUCKETS_LOWERCASE = {
        "programming_languages": SKILL_PROGRAMMING_LANGUAGE,
        "backend_frameworks": SKILL_BACKEND_FRAMEWORKS,
        "devops_technologies": SKILL_DEVOPS_TECHNOLOGIES,
        "frontend_frameworks": SKILL_FRONTEND_FRAMEWORKS,
        "system_design_skills": SKILL_SYSTEM_DESIGN,
        "version_controls": SKILL_VERSION_CONTROL,
        "ui-ux": SKILL_UI_UX,
        "data_related": SKILL_DATA_RELATED,
        "databases": SKILL_DATABASES,
        "ai_modeling": SKILL_AI_MODELING,
        "ai_frameworks": SKILL_AI_FRAMEWORKS,
        "network_skills": SKILL_NETWORK,
        "message_brokers": SKILL_MESSAGE_BROKERS,
        "hardware_skills": SKILL_HARDWARE,
        "os": SKILL_OS,
    }

    return SKILL_BUCKETS_LOWERCASE
