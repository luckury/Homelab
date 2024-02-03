#!/usr/bin/env python3

import subprocess
import glob
import yaml

def process_chart(chart_name, chart_repo, chart_src_dir, chart_render_dir):
    # Render Helm chart templates
    render_helm_chart(chart_name, chart_src_dir, chart_render_dir)

    # Extract resource kinds
    resource_kinds = extract_resource_kinds(chart_render_dir, chart_name)
    print("Extracted resource kinds:", resource_kinds)

    # Generate ArgoCD AppProject YAML
    appproject_yaml = generate_argocd_appproject_yaml(resource_kinds, chart_repo, chart_name)
    print("ArgoCD AppProject YAML:")
    print(appproject_yaml)

def render_helm_chart(chart_name, chart_directory, output_directory):
    subprocess.run(['helm', 'template', chart_name, chart_directory, '--output-dir', output_directory], check=True)

def extract_resource_kinds(output_directory, chart_name):
    resources = dict()
    
    path = rf'{output_directory}/{chart_name}/**/*.yaml'
    filenames = glob.glob(path)
    
    for filename in filenames:
        with open(filename, 'r') as f:
            manifests = yaml.safe_load_all(f)
            
            ## In case there are multiple manifests separated with '---' in one file
            for manifest in manifests:
                key = ''
                
                ## Check for top level resource kind
                if '/' not in manifest['apiVersion']:
                    key = '<empty-string>'
                else:
                    key = str(manifest['apiVersion']).split('/')[0]

                if key not in resources:
                    resources[key] = set()
                
                resources[key].add(manifest['kind'])
    
    print('resources:', resources)
    return resources

def generate_argocd_appproject_yaml(resource_kinds, chart_repo, chart_name):
    resource_kinds = dict(sorted(resource_kinds.items()))
    appproject_yaml = {
        'apiVersion': 'argoproj.io/v1alpha1',
        'kind': 'AppProject',
        'metadata': {'name': f'appproject-{chart_name}'},
        'spec': {
            'sourceRepos': [chart_repo],
            'destinations': [{'namespace': f'{chart_name}', 'server': 'https://kubernetes.default.svc'}],
            'clusterResourceWhitelist': [{'group': str(resource).replace('<empty-string>', ''), 'kind': kind} for resource in resource_kinds.keys() for kind in resource_kinds[resource]]
        }
    }
    return yaml.dump(appproject_yaml, default_flow_style=False)

if __name__ == "__main__":
    chart_name = 'cert-manager'
    chart_repo = 'https://...'
    chart_src_dir = f'tmp/charts/{chart_name}'
    chart_render_dir = 'tmp/rendered_charts/'

    process_chart(chart_name, chart_repo, chart_src_dir, chart_render_dir)
