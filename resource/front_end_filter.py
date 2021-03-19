def do(payload, config, plugin_config, inputs):

    family = config['family']
    
    choices = {
        'inverse_gaussian':[
            {'value': 'inverse_squared', 'label': 'Inverse Squared'},
            {'value': 'inverse_power', 'label': 'Inverse Power'},
            {'value': 'identity', 'label': 'Identity'},
            {'value': 'log', 'label': 'Log'}
        ],
        'gaussian':[
            {'value': 'log', 'label': 'Log'},
            {'value': 'identity', 'label': 'Identity'},
            {'value': 'inverse_power', 'label': 'Inverse Power'}
        ],
        'binomial':[
            {'value': 'logit', 'label': 'Logit'},
            {'value': 'probit', 'label': 'Probit'},
            {'value': 'cauchy', 'label': 'Cauchy'},
            {'value': 'log', 'label': 'Log'},
            {'value': 'cloglog', 'label': 'Cloglog'},
            {'value': 'identity', 'label': 'Identity'}
        ],
        'tweedie':[
            {'value': 'log', 'label': 'Log'},
            {'value': 'power', 'label': 'Power'}
        ],
        'poisson':[
            {'value': 'log', 'label': 'Log'},
            {'value': 'identity', 'label': 'Identity'},
            {'value': 'sqrt', 'label': 'Sqrt'}
        ],
        'negative_binomial':[
            {'value': 'log', 'label': 'Log'},
            {'value': 'cloglog', 'label': 'Cloglog'},
            {'value': 'identity', 'label': 'Identity'},
            {'value': 'nbinom', 'label': 'Nbinom'},
            {'value': 'power', 'label': 'Power'},
        ],
        'gamma':[
            {'value': 'log', 'label': 'Log'},
            {'value': 'identity', 'label': 'Identity'},
            {'value': 'inverse_power', 'label': 'Inverse Power'},
        ]
    }
    
    return {"choices": choices[family]}