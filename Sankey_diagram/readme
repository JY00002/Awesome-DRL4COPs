# Tutorial: Creating Sankey Diagrams from Research Paper Data Using Python and Origin

## Step 1: Prepare Your Input Data

### Data Structure Requirements
1. Create an Excel file named `input.xlsx` with your research paper data
2. Each row should represent one paper's methodology
3. Columns should represent different stages of methodology (in order from left to right)

### Recommended Columns (customize as needed):
- **Problem**: Research problem category
- **Agent**: Type of agent/model used
- **State**: State representation method
- **Embedding**: Embedding technique
- **RL**: Reinforcement learning approach
- **Action**: Action selection method
- **Year**: Publication year (optional)

### Example Data:
Problem	Agent	State	Embedding	RL	Action	Year
CJSP	SA	DG	GIN	PPO	O	2020
DJSP	SA	Matrix	CNN	D3QN	DRs	2020
CJSP	SA	DG	GNN	PPO	O	2021
CJSP	MA	HG	GAT	REINFORCE	O	2021
FFSP	SA	BG	GAT	REINFORCE	J	2021
### Important Notes:
- Maintain consistent terminology (e.g., don't mix "CNN" and "Convolutional Neural Network")
- Empty cells will be treated as "None" in the visualization
- Save your file as `input.xlsx` in your working directory

## Step 2: Run the Python Code

1. Install required packages if needed:
```bash
pip install pandas openpyxl
```
2. Run the script:
```bash
python generate_sankey_data.py
```

## Step 3: Visualize in Origin

1. **Import Data**:
   - Open Origin
   - Go to File → Import → Excel
   - Select your `output.xlsx` file

2. **Create Sankey Diagram**:
   - Select all three columns (Source, Target, Value)
   - Go to Plot → Specialized → Sankey Diagram
   - (For older versions: Plot → Statistics → Sankey)

3. **Customize Appearance**:
   - Right-click on the diagram → "Plot Details"
   - Adjust colors for different categories
   - Modify link opacity (recommended: 60-80%)
   - Set node sorting: Right-click → "Sankey Diagram" → "Node Sorting"
   - Add labels by double-clicking nodes

4. **Advanced Options**:
   - To show flow values: Plot Details → "Link" tab → Check "Show Values"
   - Adjust node width: Plot Details → "Node" tab → "Size"
   - Change orientation: Plot Details → "Layout" tab → "Direction"

## Pro Tips:

1. **Data Preparation**:
   - For better results, keep category names short but clear
   - Limit to 5-7 stages (columns) for readability
   - Merge similar methods if you have too many small flows

2. **Origin Customization**:
   - Use consistent colors for the same category across levels
   - Adjust label positions to avoid overlap
   - Export as vector graphic (EPS/PDF) for publications

3. **Troubleshooting**:
   - If links disappear, check for missing values in your data
   - If the diagram looks messy, try simplifying your categories
   - For large datasets, use the "Combine Small Flows" option in Origin

## Example Workflow:

1. Collected data from 50 ML papers → `input.xlsx`
2. Ran Python script → `output.xlsx`
3. Created Sankey diagram showing:
   - Most common paths: Problem → Agent → Method
   - Dominant approaches in each category
   - Evolution of methods over years (if Year column included)

This visualization will help you identify trends and patterns in research methodologies across different papers.
