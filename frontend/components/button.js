import { Button } from '@chakra-ui/react';
import Link from 'next/link';

function ButtonUnit(props) {
    return (
        <Link href={props.url}>
            <Button 
                color='#79c579' 
                _hover={{
                    background: '#79c579',
                    color: 'white',
                }}
                variant='ghost'
                size={props.size}
                leftIcon={props.icon}
                className={props.padding}
                onClick={props.onClick}
            >
            {props.name}
            </Button>
        </Link>
    )
}

export default ButtonUnit