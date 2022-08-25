import pandas as pd


def init_data_frame():
    model_df_x = pd.DataFrame(columns=[
        "full name",
        # Skills
        "programming_languages",
        "backend_frameworks",
        "devops_technologies",
        "frontend_frameworks",
        "system_design_skills",
        "version_controls",
        "ui-ux",
        "data_related",
        "databases",
        "ai_models",
        "ai_frameworks",
        "network_skills",
        "message_brokers",
        "hardware_skills",
        "os",
        # Educations
        "bachelor-computer engineering",
        "master-computer engineering",
        "phd-computer engineering",
        "other-majors",
        # Experiences
        "mobile developer",
        "data scientist",
        "ui-ux designer",
        "network engineer",
        "data engineer",
        "software engineer",
        "full stack developer",
        "frontend developer",
        "hardware engineer",
        "devops engineer",
        "database administrator",
    ])

    model_df_y = pd.DataFrame(columns={
        "current experience",
    })

    return model_df_x, model_df_y


def append_to_dataframe(model_df_x, model_df_y, counters, skill_buckets):
    model_df_x = model_df_x.append({
        # full name
        "full name": counters["name"],
        # skills
        'programming_languages': counters["counter_skills_programming"] / len(skill_buckets["programming_languages"]),
        "backend_frameworks": counters["counter_skills_backend"] / len(skill_buckets["backend_frameworks"]),
        "devops_technologies": counters["counter_skills_devops"] / len(skill_buckets["devops_technologies"]),
        "frontend_frameworks": counters["counter_skills_frontend"] / len(skill_buckets["frontend_frameworks"]),
        "system_design_skills": counters["counter_skills_system_design"] / len(skill_buckets["system_design_skills"]),
        "version_controls": counters["counter_skills_version_control"] / len(skill_buckets["version_controls"]),
        "ui-ux": counters["counter_skills_ui_ux"] / len(skill_buckets["ui-ux"]),
        "data_related": counters["counter_skills_data_related"] / len(skill_buckets["data_related"]),
        "databases": counters["counter_skills_databases"] / len(skill_buckets["databases"]),
        "ai_models": counters["counter_skills_ai_modeling"] / len(skill_buckets["ai_modeling"]),
        "ai_frameworks": counters["counter_skills_ai_frameworks"] / len(skill_buckets["ai_frameworks"]),
        "network_skills": counters["counter_skills_network"] / len(skill_buckets["network_skills"]),
        "hardware_skills": counters["counter_skills_message_brokers"] / len(skill_buckets["hardware_skills"]),
        "message_brokers": counters["counter_skills_hardware"] / len(skill_buckets["message_brokers"]),
        "os": counters["counter_skills_os"] / len(skill_buckets["os"]),
        # education
        'bachelor-computer engineering': counters["counter_educations_bachelor"],
        "master-computer engineering": counters["counter_educations_master"],
        "phd-computer engineering": counters["counter_educations_phd"],
        "other-majors": counters["counter_educations_other_majors"],
        # experience
        "mobile developer": counters["counter_mobile_developer"],
        "data scientist": counters["counter_data_scientist"],
        "ui-ux designer": counters["counter_ui_ux_designer"],
        "network engineer": counters["counter_network_engineer"],
        "data engineer": counters["counter_data_engineer"],
        "software engineer": counters["counter_software_engineer"],
        "full stack developer": counters["counter_fullstack_developer"],
        "frontend developer": counters["counter_frontend_developer"],
        "hardware engineer": counters["counter_hardware_engineer"],
        "devops engineer": counters["counter_devops_engineer"],
        "database administrator": counters["counter_database_administrator"],
    }, ignore_index=True)

    model_df_y = model_df_y.append({
        "current experience": counters["current_job"],
    }, ignore_index=True)

    return model_df_x, model_df_y
