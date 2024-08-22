import argparse
from main.certops.certmigration import CertMigration
from main.certops.certreader import CertReader
from main.certops.certvalidator import CertValidator
from main.renewal.renewal import Renewal
from main.renewal.autoretry import AutoRetry
from main.renewal.renewalconfig import RenewalConfig

def main():
    parser = argparse.ArgumentParser(description="Certbot Vault Integration Plugin")
    parser.add_argument("command", choices=["migrate", "read", "validate", "renew"], help="Command to execute")
    parser.add_argument("--domain", required=True, help="Domain to manage")
    
    args = parser.parse_args()

    if args.command == "migrate":
        migrate_certs(args.domain)
    elif args.command == "read":
        read_certs(args.domain)
    elif args.command == "validate":
        validate_certs(args.domain)
    elif args.command == "renew":
        renew_certs(args.domain)
    else:
        print("Invalid command")

def migrate_certs(domain):
    migrator = CertMigration(domain)
    migrator.migrate_certs()

def read_certs(domain):
    reader = CertReader(domain)
    reader.read_and_validate()

def validate_certs(domain):
    validator = CertValidator(domain)
    validator.validate_cert()

def renew_certs(domain):
    renewal = Renewal(domain)
    renewal.renew_cert()

if __name__ == "__main__":
    main()
