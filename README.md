## introduction

Develop hyper-personalized news recommendation engine for Malaysia media company

Data source: Google Analytics
Algorithm: weighted alternating least squares (WALS) 
Recommendation type: User-based collaborative filtering


## 1) cd into wals_ml_engine folder

## 2) define bucket location
```
## please change ur bucket location
export IN_BUCKET=gs://mpd-recsys/nst/bq_data/nst_recsys_output_bq.csv
```

## 3) start model training - Google Cloud instance and save the recommendations result to GCP bucket (can be configure at mltrain.sh)
```
./mltrain.sh local  ${IN_BUCKET} --data-type web_views --use-optimized --output-dir trainer
```

## Reference

https://cloud.google.com/solutions/machine-learning/recommendation-system-tensorflow-overview
