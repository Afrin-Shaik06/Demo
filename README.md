High Throughput Log Analytics & Monitoring System

## 📌 Overview
This project models a distributed log analytics system designed to handle high-throughput log streams.  
It demonstrates schema design, system architecture, and distributed processing concepts using Dask and Ray.

The system is designed to:

• Process large log datasets
• Detect anomalies
• Perform distributed computation
• Ensure scalable monitoring

## 🧩 Components
• Log Sources – Servers / Applications generating logs  
• Ingestion Layer – Distributed ingestion using Dask / Ray  
• Processing Engine – Parsing & analytics  
• Anomaly Detection – Identifying unusual patterns  
• Storage – Centralized log storage  
• Monitoring – Dashboards & alerts  

## Milestone-1 Deliverables
• System Architecture Diagram → diagrams/system_architecture.png  
• Data Flow Diagram → diagrams/data_flow.png  
• Log Schema Definition → schemas/log_schema.yaml  
• Anomaly Schema Definition → schemas/anomaly_schema.yaml

## 📂 Folder Structure
Milestone-1
│
├── schemas/
│ ├── log_schema.yaml
│ └── anomaly_schema.yaml
│
├── diagrams/
│ ├── system_architecture.png
│ └── data_flow.png
│
├── docs/
│ └── architecture.md
│
├── environment/
│ ├── requirements.txt
│ └── setup.sh
│
├── tests/
│ └── test_environment.py
│
├── screenshots/
│ ├── dask_working.png
│ ├── ray_working.png
│ └── tests_passing.png
│
├── dask_app.py
├── ray_app.py
└── README.md

---

## 🧾 Description of Components

### 1️⃣ Schemas
- `log_schema.yaml` defines the structure of log data.
- `anomaly_schema.yaml` defines the anomaly detection schema.

### 2️⃣ Diagrams
- `system_architecture.png` shows the overall system architecture.
- `data_flow.png` illustrates how data moves through the system.

### 3️⃣ Documentation
- `architecture.md` explains the system design and components in detail.

### 4️⃣ Environment Setup
- `requirements.txt` contains required Python packages.
- `setup.sh` installs the required dependencies.

### 5️⃣ Distributed Processing
- `dask_app.py` demonstrates distributed computation using Dask.
- `ray_app.py` demonstrates distributed computation using Ray.

### 6️⃣ Testing
- `test_environment.py` validates environment setup.
- Pytest is used for automated testing.

### 7️⃣ Screenshots
Screenshots are included to demonstrate:
- Successful Dask execution
- Successful Ray execution
- Successful test execution

---

## ⚙️ Installation Instructions
```bash
# Clone the repository
git clone https://github.com/Afrin-Shaik06/Demo.git

# Navigate to project folder
cd Demo

# Install required dependencies
pip install -r environment/requirements.txt
```

---

## ▶️ Running Dask Application
```bash
python dask_app.py
```
Expected Output:
• Dask scheduler starts
• Distributed computation runs
• Results are printed in terminal
---

## ▶️ Running Ray Application
```bash
python ray_app.py
```
Expected Output:
• Ray initializes local cluster
• Remote tasks execute
• Processed results displayed
---

## 🧪 Running Tests
```bash
pytest
```
Expected Output:
• All tests pass successfully
• No failures

---

## 📸 Proof of Execution

Execution screenshots are available inside the `screenshots/` folder:
- `dask_working.png`
- `ray_working.png`
- `tests_passing.png`

---

## 📚 Technologies Used

- Python 3.12
- Dask
- Ray
- Pytest
- YAML
- draw.io

---

## 👩‍💻 Author

Milestone 1 – Infosys Springboard  
High Throughput Log Analytics and Monitoring System



