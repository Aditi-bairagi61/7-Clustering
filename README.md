
## Architecture

Attach the architecture diagram. It should visually explain the flow of the system, starting from data collection to job recommendations.
![Architecture Diagram](https://github.com/Aditi-bairagi61/7-Clustering/blob/main/Architecture.drawio%20(1)-1.jpg?raw=true)



---

## Steps and Workflow

### 1. Data Collection
- **Objective**: Gather comprehensive data about job categories, roles, and skills.
- **Approach**:
  - Identified and categorized corporate job types.
  - Collected job roles for each category.
  - Extracted specific skills required for the identified job roles.
  - Created individual CSV files for each category, covering 21 categories and 1,300 job roles.
- **Outcome**: A dataset of categorized job roles and their corresponding skills.

---

### 2. Data Preprocessing
- **Objective**: Transform raw data into a usable format for analysis.
- **Approach**:
  - Converted all job roles and their specific skills into a binary matrix format:
    - `1` indicates the presence of a skill for a job role.
    - `0` indicates the absence of a skill.
  - Compiled all preprocessed data into a final dataset for analysis.
- **Outcome**: A structured dataset ready for clustering and similarity analysis.

---

### 3. Clustering
- **Objective**: Group similar job roles to simplify recommendations.
- **Approach**:
  - Applied clustering techniques to divide job roles into 21 clusters based on skills.
  - Used domain knowledge and data analysis to determine the optimal number of clusters.
  - Clusters formed represent groups of job roles with similar skill sets.
- **Outcome**: Job roles grouped into meaningful clusters for better matching.

---

### 4. Job Recommendation System
- **Objective**: Recommend relevant job roles based on user input.
- **Approach**:
  - Used a similarity measure to compare user-inputted skills with job role clusters.
  - Recommended job roles ranked by relevance to the user's skills.
- **Outcome**: An AI-powered recommendation system providing job suggestions tailored to user skills.

---

### 5. Visualization
- **Objective**: Gain insights into job clusters and their skill distributions.
- **Approach**:
  - Reduced dataset dimensions for visualization using techniques like PCA and t-SNE.
  - Visualized clusters as scatterplots to illustrate the distribution of job roles and their relationships.
- **Outcome**: Clear and intuitive visual representations of job role clusters.

---

### 6. Cluster Analysis
- **Objective**: Understand the composition and dominant skills within each cluster.
- **Approach**:
  - Analyzed the data points in each cluster.
  - Identified top skills prevalent in each cluster to understand their characteristics.
- **Outcome**: Insights into the key skills driving each job role cluster.

---

## Project Files
| File Name                  | Description                                    |
|----------------------------|------------------------------------------------|
| `all_skills_matrix.csv`    | Final dataset with a binary matrix of skills.  |
| `Architecture.drawio.pdf`  | Architecture diagram for the system.           |
| `job_recommendation.py`    | Script to cluster data and recommend jobs.     |



