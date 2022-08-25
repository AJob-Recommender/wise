import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.preprocessing import LabelEncoder
from fastapi import FastAPI

import counters as cs
import dataframe
import education_buckets
import experience_buckets
import skill_buckets
import Items

"""
Reading the dataset
"""

"""
Creating the dataframe
"""
items = Items.Items

app = FastAPI()


@app.post("/predict/")
async def predict(item: items):
    data = pd.read_json("dataset/data.json")

    skills_lowercase = None
    model_df_x, model_df_y = dataframe.init_data_frame()
    for index, row in data.iterrows():
        counters = cs.init_counters()
        counted_skills = skill_buckets.init_skill_counts()
        skills_lowercase = skill_buckets.skills_to_lowercase()
        educations = education_buckets.init_educations()
        experiences = experience_buckets.init_experiences()
        # Full name
        counters["name"] = row["Full Name"]

        # Skills
        for itemSkill in row["Skills"]:
            for idx, value in enumerate(skills_lowercase["programming_languages"]):
                if itemSkill.lower() in skills_lowercase["programming_languages"][idx]:
                    if not counted_skills["programming_languages"][idx]:
                        counters["counter_skills_programming"] += 1
                        counted_skills["programming_languages"][idx] = True

            for idx, value in enumerate(skills_lowercase["backend_frameworks"]):
                if itemSkill.lower() in skills_lowercase["backend_frameworks"][idx]:
                    if not counted_skills["backend_frameworks"][idx]:
                        counters["counter_skills_backend"] += 1
                        counted_skills["backend_frameworks"][idx] = True

            for idx, value in enumerate(skills_lowercase["devops_technologies"]):
                if itemSkill.lower() in skills_lowercase["devops_technologies"][idx]:
                    if not counted_skills["devops_technologies"][idx]:
                        counters["counter_skills_devops"] += 1
                        counted_skills["devops_technologies"][idx] = True

            for idx, value in enumerate(skills_lowercase["frontend_frameworks"]):
                if itemSkill.lower() in skills_lowercase["frontend_frameworks"][idx]:
                    if not counted_skills["frontend_frameworks"][idx]:
                        counters["counter_skills_frontend"] += 1
                        counted_skills["frontend_frameworks"][idx] = True

            for idx, value in enumerate(skills_lowercase["system_design_skills"]):
                if itemSkill.lower() in skills_lowercase["system_design_skills"][idx]:
                    if not counted_skills["system_design_skills"][idx]:
                        counters["counter_skills_system_design"] += 1
                        counted_skills["system_design_skills"][idx] = True

            for idx, value in enumerate(skills_lowercase["version_controls"]):
                if itemSkill.lower() in skills_lowercase["version_controls"][idx]:
                    if not counted_skills["version_controls"][idx]:
                        counters["counter_skills_version_control"] += 1
                        counted_skills["version_controls"][idx] = True

            for idx, value in enumerate(skills_lowercase["ui-ux"]):
                if itemSkill.lower() in skills_lowercase["ui-ux"][idx]:
                    if not counted_skills["ui-ux"][idx]:
                        counters["counter_skills_ui_ux"] += 1
                        counted_skills["ui-ux"][idx] = True

            for idx, value in enumerate(skills_lowercase["data_related"]):
                if itemSkill.lower() in skills_lowercase["data_related"][idx]:
                    if not counted_skills["data_related"][idx]:
                        counters["counter_skills_data_related"] += 1
                        counted_skills["data_related"][idx] = True

            for idx, value in enumerate(skills_lowercase["databases"]):
                if itemSkill.lower() in skills_lowercase["databases"][idx]:
                    if not counted_skills["databases"][idx]:
                        counters["counter_skills_databases"] += 1
                        counted_skills["databases"][idx] = True

            for idx, value in enumerate(skills_lowercase["ai_modeling"]):
                if itemSkill.lower() in skills_lowercase["ai_modeling"][idx]:
                    if not counted_skills["ai_modeling"][idx]:
                        counters["counter_skills_ai_modeling"] += 1
                        counted_skills["ai_modeling"][idx] = True

            for idx, value in enumerate(skills_lowercase["ai_frameworks"]):
                if itemSkill.lower() in skills_lowercase["ai_frameworks"][idx]:
                    if not counted_skills["ai_frameworks"][idx]:
                        counters["counter_skills_ai_frameworks"] += 1
                        counted_skills["ai_frameworks"][idx] = True

            for idx, value in enumerate(skills_lowercase["network_skills"]):
                if itemSkill.lower() in skills_lowercase["network_skills"][idx]:
                    if not counted_skills["network_skills"][idx]:
                        counters["counter_skills_network"] += 1
                        counted_skills["network_skills"][idx] = True

            for idx, value in enumerate(skills_lowercase["message_brokers"]):
                if itemSkill.lower() in skills_lowercase["message_brokers"][idx]:
                    if not counted_skills["message_brokers"][idx]:
                        counters["counter_skills_message_brokers"] += 1
                        counted_skills["message_brokers"][idx] = True

            for idx, value in enumerate(skills_lowercase["hardware_skills"]):
                if itemSkill.lower() in skills_lowercase["hardware_skills"][idx]:
                    if not counted_skills["hardware_skills"][idx]:
                        counters["counter_skills_hardware"] += 1
                        counted_skills["hardware_skills"][idx] = True

            for idx, value in enumerate(skills_lowercase["os"]):
                if itemSkill.lower() in skills_lowercase["os"][idx]:
                    if not counted_skills["os"][idx]:
                        counters["counter_skills_os"] += 1
                        counted_skills["os"][idx] = True

        for itemEducation in row["Educations"]:
            if itemEducation["major"] == educations[0]:
                counters["counter_educations_bachelor"] = 1
            if itemEducation["major"] == educations[1]:
                counters["counter_educations_master"] = 1
            if itemEducation["major"] == educations[2]:
                counters["counter_educations_phd"] = 1
            if itemEducation["major"] == educations[3]:
                counters["counter_educations_other_majors"] = 1

        for i in range(len(row["Experiences"])):
            if len(row["Experiences"]) == 1:
                counters["current_job"] = (row["Experiences"][i])["name"]
            else:
                counters["current_job"] = (row["Experiences"][0])["name"]
                if i != 0:
                    if (row["Experiences"][i])["name"] == experiences[0]:
                        counters["counter_mobile_developer"] += 1
                    if (row["Experiences"][i])["name"] == experiences[1]:
                        counters["counter_data_scientist"] += 1
                    if (row["Experiences"][i])["name"] == experiences[2]:
                        counters["counter_ui_ux_designer"] += 1
                    if (row["Experiences"][i])["name"] == experiences[3]:
                        counters["counter_network_engineer"] += 1
                    if (row["Experiences"][i])["name"] == experiences[4]:
                        counters["counter_data_engineer"] += 1
                    if (row["Experiences"][i])["name"] == experiences[5]:
                        counters["counter_software_engineer"] += 1
                    if (row["Experiences"][i])["name"] == experiences[6]:
                        counters["counter_fullstack_developer"] += 1
                    if (row["Experiences"][i])["name"] == experiences[7]:
                        counters["counter_frontend_developer"] += 1
                    if (row["Experiences"][i])["name"] == experiences[8]:
                        counters["counter_hardware_engineer"] += 1
                    if (row["Experiences"][i])["name"] == experiences[9]:
                        counters["counter_devops_engineer"] += 1
                    if (row["Experiences"][i])["name"] == experiences[10]:
                        counters["counter_database_administrator"] += 1

        model_df_x, model_df_y = dataframe.append_to_dataframe(model_df_x, model_df_y, counters, skills_lowercase)

    model_df_x.to_csv('dataframe/df_x.csv', index=False)
    model_df_y.to_csv('dataframe/df_y.csv', index=False)

    """
    Importing dataframes
    """
    df_x = pd.read_csv("dataframe/df_x.csv")
    df_y = pd.read_csv("dataframe/df_y.csv")

    df_y["current experience"] = df_y["current experience"].fillna("")
    indexes = df_y.loc[(df_y["current experience"] == "") | (df_y["current experience"] == "others")].index
    df_y.drop(df_y[(df_y["current experience"] == "") | (df_y["current experience"] == "others")].index, inplace=True)
    df_x.drop(indexes, inplace=True)

    print("asliii: ", np.shape(df_x))
    le = LabelEncoder()
    train_x = df_x.iloc[:, 1:].values.tolist()
    train_y = df_y.values.ravel()
    train_y = le.fit_transform(train_y)
    print("shape train: ", np.shape(train_x))

    x_train, x_test, y_train, y_test = train_test_split(train_x, train_y, shuffle=True, test_size=0.20, random_state=0)

    clf = tree.DecisionTreeClassifier()
    clf.fit(x_train, y_train)

    cv = KFold(n_splits=20, random_state=1, shuffle=True)
    scores = cross_val_score(clf, x_train, y_train, cv=cv)

    prediction = clf.predict(x_test)
    df_x_test, df_y_test = dataframe.init_data_frame()

    df_x_test = df_x_test.append({
        "full name": "amir",
        "programming_languages": sum(item.programming_languages.values()) / len(skills_lowercase["programming_languages"]),
        "backend_frameworks": sum(item.backend_frameworks.values()) / len(skills_lowercase["backend_frameworks"]),
        "devops_technologies": sum(item.devops_technologies.values()) / len(skills_lowercase["devops_technologies"]),
        "frontend_frameworks": sum(item.frontend_frameworks.values()) / len(skills_lowercase["frontend_frameworks"]),
        "system_design_skills": sum(item.system_design_skills.values()) / len(skills_lowercase["system_design_skills"]),
        "version_controls": sum(item.version_controls.values()) / len(skills_lowercase["version_controls"]),
        "ui-ux": sum(item.ui_ux.values()) / len(skills_lowercase["ui-ux"]),
        "data_related": sum(item.data_related.values()) / len(skills_lowercase["data_related"]),
        "databases": sum(item.databases.values()) / len(skills_lowercase["databases"]),
        "ai_frameworks": sum(item.ai_frameworks.values()) / len(skills_lowercase["ai_frameworks"]),
        "ai_models": sum(item.ai_models.values()) / len(skills_lowercase["ai_modeling"]),
        "network_skills": sum(item.network_skills.values()) / len(skills_lowercase["network_skills"]),
        "message_brokers": sum(item.message_brokers.values()) / len(skills_lowercase["message_brokers"]),
        "hardware_skills": sum(item.hardware_skills.values()) / len(skills_lowercase["hardware_skills"]),
        "os": sum(item.os.values()) / len(skills_lowercase["os"]),
        "bachelor-computer engineering": sum(item.bachelor_computer_engineering.values()),
        "master-computer engineering": sum(item.master_computer_engineering.values()),
        "phd-computer engineering": sum(item.phd_computer_engineering.values()),
        "other-majors": sum(item.other_majors.values()),
        # Experiences
        "mobile developer": sum(item.mobile_developers.values()),
        "data scientist": sum(item.data_scientists.values()),
        "ui-ux designer": sum(item.ui_ux_designer.values()),
        "network engineer": sum(item.network_engineer.values()),
        "data engineer": sum(item.data_engineer.values()),
        "software engineer": sum(item.software_engineer.values()),
        "full stack developer": sum(item.fullstack_developer.values()),
        "frontend developer": sum(item.frontend_developer.values()),
        "hardware engineer": sum(item.hardware_engineer.values()),
        "devops engineer": sum(item.devops_engineer.values()),
        "database administrator": sum(item.database_administrator.values()),
    }, ignore_index=True)

    print("dataframe: ", np.shape(df_x_test))
    d = df_x_test.iloc[:, 1:].values.tolist()
    print("d: ", np.shape(d))
    print("shape: ", np.shape(df_x_test.iloc[:, 1:].values.tolist()))
    job_encoded = clf.predict(df_x_test.iloc[:, 1:].values.tolist())
    print("job encoded: ", le.inverse_transform(job_encoded))

    job = le.inverse_transform(job_encoded)

    return {
        "job": job[0],
    }

