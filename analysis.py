# Calculating a composite risk score by summing relevant risk scores
risk_columns = [col for col in data.columns if 'risk_score' in col]
data['composite_risk_score'] = data[risk_columns].sum(axis=1)

# Calculating an inconsistency index by summing relevant inconsistency indicators
inconsistency_columns = [
    'income_inconsistency', 
    'application_bureau_data_inconsistency_score', 
    'address_mismatch_indicator'
]

# Assuming 'income_inconsistency', 'address_mismatch_indicator', and 'application_bureau_data_inconsistency_score' exist
# If not, create a simple sum from relevant columns
inconsistency_columns = [col for col in inconsistency_columns if col in data.columns]
data['inconsistency_index'] = data[inconsistency_columns].sum(axis=1)

# Set thresholds based on a percentile of the composite scores
risk_threshold = data['composite_risk_score'].quantile(0.95)
inconsistency_threshold = data['inconsistency_index'].quantile(0.95)

# Apply initial filtering strategy
data['strategy_hit_indicator'] = (
    (data['composite_risk_score'] >= risk_threshold) &
    (data['inconsistency_index'] >= inconsistency_threshold)
).astype(int)

# Count number of variables used
data['no_of_vars'] = len(risk_columns) + len(inconsistency_columns)

# Prepare the final output
final_output = data[['unique_identifier', 'strategy_hit_indicator', 'no_of_vars']]

# Display the final output to the user
import ace_tools as tools; tools.display_dataframe_to_user(name="Final Strategy Output", dataframe=final_output)

# Save the output for final submission
final_output_path = '/mnt/data/final_strategy_output.csv'
final_output.to_csv(final_output_path, index=False)

final_output_path
