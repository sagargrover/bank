cd /bank
cp ops/yaml/config.yml .
apt-get update
apt -y install software-properties-common
pip install -r requirements.txt
mkdir -p /bank/logs
export PYTHONPATH="${PYTHONPATH}:/bank/"