from fastapi import FastAPI
from joblib import load
import dataframe
import experience_buckets
import skill_buckets
import Items

items = Items.Items

app = FastAPI()


@app.post("/predict")
async def predict(item: items):
    skills_lowercase = skill_buckets.skills_to_lowercase()
    experiences = experience_buckets.init_experiences()

    clf = load('pipeline/gradient_boosting.joblib')

    df_x_test, df_y_test = dataframe.init_data_frame()

    df_x_test = df_x_test.append({
        "programming_languages": sum(item.programming_languages.values()) / len(
            skills_lowercase["programming_languages"]),
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
        "hardware_skills": sum(item.hardware_skills.values()) / len(skills_lowercase["hardware_skills"]),
        "bachelor-computer engineering": sum(item.bachelor_computer_engineering.values()),
        "master-computer engineering": sum(item.master_computer_engineering.values()),
        "phd-computer engineering": sum(item.phd_computer_engineering.values()),
        "other-majors": sum(item.other_majors.values()),
        # Experiences
        "data scientist": sum(item.data_scientists.values()),
        "ui-ux designer": sum(item.ui_ux_designer.values()),
        "network engineer": sum(item.network_engineer.values()),
        "data engineer": sum(item.data_engineer.values()),
        "software engineer": sum(item.software_engineer.values()),
        "frontend developer": sum(item.frontend_developer.values()),
        "hardware engineer": sum(item.hardware_engineer.values()),
        "devops engineer": sum(item.devops_engineer.values()),
        "database administrator": sum(item.database_administrator.values()),
    }, ignore_index=True)

    # Predicting the results
    results = clf.predict_proba(df_x_test.iloc[:, 1:].values.tolist())

    probabilities = {
        experiences[0]: results[0][0],
        experiences[1]: results[0][1],
        experiences[2]: results[0][2],
        experiences[3]: results[0][3],
        experiences[4]: results[0][4],
        experiences[5]: results[0][5],
        experiences[6]: results[0][6],
        experiences[7]: results[0][7],
        experiences[8]: results[0][8],
    }
    sorted_dict = {}
    sorted_keys = sorted(probabilities, key=probabilities.get, reverse=True)

    for w in sorted_keys:
        sorted_dict[w] = probabilities[w]

    result = [
        {
            "job": list(sorted_dict.keys())[0],
            "confidence": sorted_dict[list(sorted_dict.keys())[0]] * 100
        },
        {
            "job": list(sorted_dict.keys())[1],
            "confidence": sorted_dict[list(sorted_dict.keys())[1]] * 100
        },
        {
            "job": list(sorted_dict.keys())[2],
            "confidence": sorted_dict[list(sorted_dict.keys())[2]] * 100
        }
    ]

    return {
        "results": result
    }

