import { Button } from '@chakra-ui/react';

function ButtonUnit(props) {
    return (
        <Button 
            color='#79c579' 
            _hover={{
                background: '#79c579',
                color: 'white',
            }}
            variant='ghost'
            size={props.size}
            leftIcon={props.icon}
        >
        {props.name}
        </Button>
    )
}

export default ButtonUnit