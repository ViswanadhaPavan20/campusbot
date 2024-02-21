from langchain_community.document_loaders import WebBaseLoader
def clean_main(doc):
  header = "         SR Gudlavalleru Engineering College | An Autonomous Institute                                    Admission Enquiry Form       Latest News :       Student Development Programme  on  Business Analytics – Power BI and R  Software 6-11 January, 2024   In view of the prevailing climatic conditions, the National level Literary and Cultural events Contest scheduled during 7-8,December is postponed. Further schedule will be intimated later.   A National Level Inter-Engineering Collegiate Tournament on 18-20 Nov, 2023(Registration Last Date: 15, Nov 2023)    SRGEC Ratnas Awards (Extended Upto 15-11-2023)   Placements for the Class of 2023 – 890* (as on 21st August 2023) (CIVIL-27, EEE-80, ME-98, ECE-285, CSE-265, IT-78, MBA-57).   Student Background Verification Circular   IMPORTANT Notice: All Education Verification requests should be sent to verifications@gecgudlavalleru.ac.in             News & Updates    Downloads    Links                                 About GEC   About us Promoters Vision and Mission   Administration   Chairman Secretary & Correspondent Principal Vice Principals    Directors  AS&A PGCRD   Quality Policy Imp Contact Numbers    Why GEC?   Accreditations Awards Best Practices Institutional Distinctiveness Future Plans    Academics   Departments  Programmes Offered   UG Programmes PG Programmes    Admission Procedure Fee Details Rules And Regulations Academic calendar  Academic Awards  College Publications    Examinations   CoE Assistant COEs Regulations Examination Rules Circulars   B.Tech M.Tech MBA   Fee Notifications   B.Tech M.Tech MBA    Results   B.Tech M.Tech MBA    Time Tables    B.Tech M.Tech MBA   Downloads(AT) Contact Us    Placements   Goals and Objectives MOUS Training programs Esteemed Recruiters Placement Statistics Assessment Partners Office Bearers Downloads    R&D   Research Ethics Committee Research Promotion Policy Seed Money (In-House R&D Projects) External Funded Projects Consultancy Publications PhD Guidance     Facilities    Central Library   At a Glance Dept wise Books Info Journals Library Committee  Self Learning Courses NPTEL Web Courses Videos Remote Access    Infrastructure   Class Rooms Laboratories Seminar Halls Central Lecture Theatre  Geo Tagged Photos    Amenities Block   Gymnasium Indoor Stadium Built up area Guest Rooms  Canteen    Physical Education   Staff University Blues Achievements Facilities Fitness Center    NSS   NSS Committee Events Organized    Transportation Faculty Club Hostels  Others   Internet WI-FI Bank & ATM       Alumni   Alumni Website About Alumni Faculty Coordinators Alumni Office bearers Alumni Meet Alumni Activities DISA a way forward Scholarships Eminent Alumni   Gallery  NAAC-2023  SSR IIQA DVV   Library SRGEC Ratnas Awards Silver Jubilee Feedback Contact Us       A- A A+"
  footer = "Testimonials     Nice college ,good atmosphere,great library Completed my graduation (B.Tech) (EEE)2014-2018 batch.   kunamneni raghu pradeep( EEE )     One of the best infrastructured college in AP. Students has a huge platform to reach their goals by well qualified lecturers.   Dheeraj korukonda( CSE )     Very good college with infrastructure , experienced faculty. College library is top among the libraries of andhrapradesh. Amenities(canteen, internal auditorium, play ground) for students are awesome.   vinay sairam( Google Review )          Quick Links    Ecap College Administration Imp Phone Numbers Departments Academic Calender Fee Details     Smart India Hackathon GEC RESULTS College News Letter ARIIA Reports-2022 RTI Cell Central Library            Contact us      Seshadri Rao Gudlavalleru Engineering College, Seshadri Rao Knowledge Village, Gudlavalleru, Krishna(dt), Andhra Pradesh 521356.  08674-273737 / 273888, +91 9848779121   08674-273957,   principal@gecgudlavalleru.ac.in       Location   How to reach us                 Last Updated 03 October 2023    Vistors Counter :                                    © 2024 SR Gudlavalleru Engineering College | An Autonomous Institute. All rights reserved | Made with  by SR Gudlavalleru Engineering College          Home About GEC  About us Promoters College Administration Governing Body Academic Council IQAC Members  Administration  Chairman Secretary & Correspondent Principal Vice Principal    Directors  AS&A PGCRD    Quality Policy Imp Contact Numbers    Why GEC?  Accreditations Awards    Academics  Departments  Programmes Offered  UG Programmes PG Programmes    Admission Procedure Rules And Regulations Academic calendar Academic Awards    Examinations  CoE Assistant COEs Regulations Examination Rules  Fee Notifications  B.Tech M.Tech MBA     Results  B.Tech M.Tech MBA     Time Tables  B.Tech M.Tech MBA    Downloads(AT) Contact Us    Placements  Goals and Objectives MOUS Training programs Esteemed Recruiters Placement Statistics Assessment Partners Office Bearers Downloads    R&D  Research Ethics Committee Research Promotion Policy Seed Money (In-House R&D Projects) External Funded Projects Consultancy Publications PhD Guidance     Facilities   Central Library  At a Glance Dept wise Books Info Journals Library Committee  NPTEL Web Courses Videos    Infrastructure  Class Rooms Laboratories Seminar Halls Central Lecture Theatre     Amenities Block  Gymnasium Indoor Stadium Built up area Guest Rooms  Canteen    Physical Education   Staff University Blues Events Organized Facilities Fitness Center    NSS  Events Organized NSS Regular Activities NSS Special Camp   Transportation Faculty Club Hostels  Others  Internet WI-FI Bank & ATM      Alumni  About Alumni Faculty Coordinators Alumni Office bearers Alumni Meet Alumni Activities DISA a way forward Scholarships Eminent Alumni   Gallery  NAAC-2023  SSR IIQA DVV   Library Silver Jubilee Feedback Contact Us"
  sidebar = "About GEC  About us Promoters Vision and Mission Governing Body Academic Council  Administration   Chairman Secretary & Correspondent Principal Vice Principals   Directors   AS&A PGCRD   Innovation and Entrepreneurship Pre Incubation and Innovation Centers Innovation and Incubation Cell Quality Policy Imp Contact Numbers"
  doc.page_content = doc.page_content.replace("\n"," ")
  doc.page_content = doc.page_content.replace(header," ")
  doc.page_content = doc.page_content.replace(footer," ")
  doc.page_content = doc.page_content.replace(sidebar," ")
  return doc

def iot_clean(doc):
  header = "SR Gudlavalleru Engineering College                             Latest News :       Five-day SDP Program on Python for IoT : Connecting the physical World Organised by the Department of Internet of Things from 14-11-2023 to 18-11-2023   Two-Day National Level Technical Competition FUSIONX-2k23 (14-9-2023 to 15-9-2023)   Three - Day SDP on Real Time IoT Applications using Advanced Microcontrollers (24-8-2023 to 26-8-2023)   One-Week International Faculty Development Programme on IoT, Industry 4.0 and Stress Management  from 17-07-2023 to 22-07-2023    Three-Day Intensive IoT Workshop and Hackathon on Internet of Things  from 11-07-2023 to 13-07-2023.                                  GEC   Home   faculty   Infrastructure   LABS Classrooms  Department Library     Academic Info   R&D  Advisory Committee Committee Members Projects                                    IN-HOUSE R&D PROJECTS EXTERNAL FUNDED PROJECTS    Funded Schemes Publications     Department Activities   Student Activities                                    PATRIOT ACTIVITIES DRONE CLUB ACTIVITIES ISF ACTIVITIES SDP ACTIVITIES    Faculty Activities Summary of Student Activities Summary of Faculty Activities     Placements   Alumni   Alumni List Suggestions Alumni Activities     Gallery   Contact Us"
  footer = "Opening Hours    Mon - Fri :  9.00 am - 6.00 pm  Saturday : 9.00 am - 5.00 pm  Sun :\xa0 \xa0Closed       Quick Links    Infrastructure    Academic Info   Placements   faculty       Address    SR Gudlavalleru Engineering College, Gudlavalleru, Krishna Dist, Andhra Pradesh, INDIA. 521356     08674-273737     hod.iot@gecgudlavalleru.ac.in            Last Updated  31  January  2024           Â© 2024 SR Gudlavalleru Engineering College             GEC   Home   faculty  Infrastructure  LABS Classrooms  Department Library    Academic Info   R&D  Advisory Committee Committee Members  Projects  IN-HOUSE R&D PROJECTS EXTERNAL FUNDED PROJECTS      Department Activities  Student Activities  PATRIOT ACTIVITIES DRONE CLUB ACTIVITIES ISF ACTIVITIES SDP ACTIVITIES HELPING HANDS   Faculty Activities    Placements   Alumni  Alumin List Suggetions    Gallery   Contact Us"
  footer2 ="Opening Hours    Mon - Fri :  9.00 am - 6.00 pm  Saturday : 9.00 am - 5.00 pm  Sun :\xa0 \xa0Closed       Quick Links    Infrastructure    Academic Info   Placements   faculty       Address    SR Gudlavalleru Engineering College, Gudlavalleru, Krishna Dist, Andhra Pradesh, INDIA. 521356     08674-273737     hod.iot@gecgudlavalleru.ac.in            Last Updated  31  January  2024           © 2024 SR Gudlavalleru Engineering College             GEC   Home   faculty  Infrastructure  LABS Classrooms  Department Library    Academic Info   R&D  Advisory Committee Committee Members  Projects  IN-HOUSE R&D PROJECTS EXTERNAL FUNDED PROJECTS      Department Activities  Student Activities  PATRIOT ACTIVITIES DRONE CLUB ACTIVITIES ISF ACTIVITIES SDP ACTIVITIES HELPING HANDS   Faculty Activities    Placements   Alumni  Alumin List Suggetions    Gallery   Contact Us" 
  doc.page_content = doc.page_content.replace("\n"," ")
  doc.page_content = doc.page_content.replace(header," ")
  doc.page_content = doc.page_content.replace("view more", " ")
  doc.page_content = doc.page_content.replace(footer," ")
  doc.page_content = doc.page_content.replace(footer2," ")
  return doc

def get_data():
    iot_urls = [
    "https://iot.gecgudlavalleru.ac.in/",
    "https://iot.gecgudlavalleru.ac.in/facaulty",
    "https://iot.gecgudlavalleru.ac.in/infrastructure_labs/IoT-based-Embedded-Systems-Laboratory",
    "https://iot.gecgudlavalleru.ac.in/classrooms",
    "https://iot.gecgudlavalleru.ac.in/department_library",
    "https://iot.gecgudlavalleru.ac.in/advisory_committee",
    "https://iot.gecgudlavalleru.ac.in/committee_members",
    "https://iot.gecgudlavalleru.ac.in/projects/IN-HOUSE-R-D-PROJECTS",
    "https://iot.gecgudlavalleru.ac.in/project_details/IN-HOUSE-R-D-PROJECTS/6jSAp_Smart-Agriculture-Monitoring-System-Using-LoRAWAN-Internet-of-Things-and-Artificial-Intelligence-Analysis",
    "https://iot.gecgudlavalleru.ac.in/project_details/IN-HOUSE-R-D-PROJECTS/IetAQ_Design-and-Implementation-of-Facial-recognition-using-Drone-Technology",
    "https://iot.gecgudlavalleru.ac.in/projects/EXTERNAL-FUNDED-PROJECTS",
    "https://iot.gecgudlavalleru.ac.in/project_details/EXTERNAL-FUNDED-PROJECTS/rGytq_Design-of-Operational-Trans-Conductance-Amplifier-for-ECG-Applications-using-CMOS-Technology-OTA-RPS-",
    "https://iot.gecgudlavalleru.ac.in/funded_schemes",
    "https://iot.gecgudlavalleru.ac.in/funded_details/Soft-Computing-Techniques-and-it-s-Applications",
    "https://iot.gecgudlavalleru.ac.in/funded_details/Prerana",
    "https://iot.gecgudlavalleru.ac.in/funded_details/AICTE-MODROBS-Modernization-of-Database-Lab",
    "https://iot.gecgudlavalleru.ac.in/publications",
    "https://iot.gecgudlavalleru.ac.in/student_activities/SDP-ACTIVITIES",
    "https://iot.gecgudlavalleru.ac.in/faculty_activities",
    "https://iot.gecgudlavalleru.ac.in/summary_activities",
    "https://iot.gecgudlavalleru.ac.in/summary_faculty_activities",
    "https://iot.gecgudlavalleru.ac.in/contact",
    # "https://iot.gecgudlavalleru.ac.in/e_content",
    "https://iot.gecgudlavalleru.ac.in/syllabus"
    ]

    main_page_urls = [
    "https://www.gecgudlavalleru.ac.in/",
    "https://gecgudlavalleru.ac.in/principal.php",
    "https://gecgudlavalleru.ac.in/chairman.php",
    "https://gecgudlavalleru.ac.in/profile_of_vvsr.php",
    "https://gecgudlavalleru.ac.in/awards.php",
    "https://gecgudlavalleru.ac.in/induction_progrmme.php"
    ]


    ## Main Pages Data
    loader = WebBaseLoader(main_page_urls)
    main_docs = loader.load()

    # for i in range(1, len(main_docs)):
    for i in range(len(main_docs)):
        clean_main(main_docs[i])

    h1 = "About GEC   About us Promoters Vision and Mission   Administration   Chairman Secretary & Correspondent Principal Vice Principals    Directors  AS&A PGCRD   Quality Policy Imp Contact Numbers    Why GEC?   Accreditations Awards Best Practices Institutional Distinctiveness Future Plans    Academics   Departments  Programmes Offered   UG Programmes PG Programmes    Admission Procedure Fee Details Rules And Regulations Academic calendar  Academic Awards  College Publications    Examinations   CoE Assistant COEs Regulations Examination Rules Circulars   B.Tech M.Tech MBA   Fee Notifications   B.Tech M.Tech MBA    Results   B.Tech M.Tech MBA    Time Tables    B.Tech M.Tech MBA   Downloads(AT) Contact Us"
    f1 = "Last Updated 03 October 2023    Vistors Counter :                                    © 2024 SR Gudlavalleru Engineering College | An Autonomous Institute. All rights reserved | Made with  by SR Gudlavalleru Engineering College          Home About GEC  About us Promoters College Administration Governing Body Academic Council IQAC Members  Administration  Chairman Secretary & Correspondent Principal Vice Principal    Directors  AS&A PGCRD    Quality Policy Imp Contact Numbers    Why GEC?  Accreditations Awards    Academics  Departments  Programmes Offered  UG Programmes PG Programmes    Admission Procedure Rules And Regulations Academic calendar Academic Awards    Examinations  CoE Assistant COEs Regulations Examination Rules  Fee Notifications  B.Tech M.Tech MBA     Results  B.Tech M.Tech MBA     Time Tables  B.Tech M.Tech MBA    Downloads(AT) Contact Us    Placements  Goals and Objectives MOUS Training programs Esteemed Recruiters Placement Statistics Assessment Partners Office Bearers Downloads    R&D  Research Ethics Committee Research Promotion Policy Seed Money (In-House R&D Projects) External Funded Projects Consultancy Publications PhD Guidance     Facilities   Central Library  At a Glance Dept wise Books Info Journals Library Committee  NPTEL Web Courses Videos    Infrastructure  Class Rooms Laboratories Seminar Halls Central Lecture Theatre     Amenities Block  Gymnasium Indoor Stadium Built up area Guest Rooms  Canteen    Physical Education   Staff University Blues Events Organized Facilities Fitness Center    NSS  Events Organized NSS Regular Activities NSS Special Camp   Transportation Faculty Club Hostels  Others  Internet WI-FI Bank & ATM      Alumni  About Alumni Faculty Coordinators Alumni Office bearers Alumni Meet Alumni Activities DISA a way forward Scholarships Eminent Alumni   Gallery  NAAC-2023  SSR IIQA DVV   Library Silver Jubilee Feedback Contact Us"
    main_docs[0].page_content = main_docs[0].page_content.replace("\n"," ")
    main_docs[0].page_content = main_docs[0].page_content.replace(h1," ")
    main_docs[0].page_content = main_docs[0].page_content.replace(f1," ")
    main_docs[0].page_content = main_docs[0].page_content.replace("08674-273957", " ")
    main_docs[0].page_content = "Principal of SRGEC" + main_docs[0].page_content
    

    ## IoT Pages Data
    loader = WebBaseLoader(iot_urls)
    iot_docs = loader.load()

    for i in range(2, len(iot_docs)):
        iot_clean(iot_docs[i])

    h2 = "GEC   Home   faculty   Infrastructure   LABS Classrooms  Department Library     Academic Info   R&D  Advisory Committee Committee Members Projects                                    IN-HOUSE R&D PROJECTS EXTERNAL FUNDED PROJECTS    Funded Schemes Publications     Department Activities   Student Activities                                    PATRIOT ACTIVITIES DRONE CLUB ACTIVITIES ISF ACTIVITIES SDP ACTIVITIES    Faculty Activities Summary of Student Activities Summary of Faculty Activities     Placements   Alumni   Alumni List Suggestions Alumni Activities     Gallery   Contact Us"
    f2 = "Last Updated  31  January  2024           © 2024 SR Gudlavalleru Engineering College             GEC   Home   faculty  Infrastructure  LABS Classrooms  Department Library    Academic Info   R&D  Advisory Committee Committee Members  Projects  IN-HOUSE R&D PROJECTS EXTERNAL FUNDED PROJECTS      Department Activities  Student Activities  PATRIOT ACTIVITIES DRONE CLUB ACTIVITIES ISF ACTIVITIES SDP ACTIVITIES HELPING HANDS   Faculty Activities    Placements   Alumni  Alumin List Suggetions    Gallery   Contact Us"
    # IoT Main Page
    iot_docs[0].page_content = iot_docs[0].page_content.replace("\n"," ")
    iot_docs[0].page_content = iot_docs[0].page_content.replace(h2," ")
    iot_docs[0].page_content = iot_docs[0].page_content.replace(f2," ")

    # IoT Faculty Page
    iot_docs[1].page_content = "They are Faculty of IoT Department: \n\n\n" + iot_docs[1].page_content
    ## Combining Main and IoT Pages
    documents = main_docs + iot_docs

    return documents