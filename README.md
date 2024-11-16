
# Job Recommendation System using AI

This project leverages AI techniques to recommend job roles based on user-provided skills. It uses data clustering and similarity-based matching to enhance the accuracy of recommendations. The following sections outline the methodology, steps, and insights gained during the development of the project.

---

## Architecture

Attach the architecture diagram (use `Architecture.drawio.pdf` for the GitHub repository). It should visually explain the flow of the system, starting from data collection to job recommendations.

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

---

## How to Run the Project
1. **Clone the Repository**: Download the project files to your local machine.
2. **Install Dependencies**: Use a package manager to install required Python libraries (e.g., Pandas, Scikit-learn).
3. **Run the System**: Execute the script to see job recommendations based on user-inputted skills.
4. **Visualize Clusters**: Run the visualization steps to explore the structure of the job clusters.

---

## Future Work
- **Expand Data Coverage**: Include more job categories and skills to improve recommendations.
- **Integrate with External Platforms**: Connect the system with LinkedIn or job portals for real-time updates.
- **Enhance Clustering**: Explore advanced clustering algorithms for better accuracy.
- **Develop an API**: Create an API to enable external integration and real-time user interaction.

---
