import { Flex } from '@chakra-ui/react';
import ButtonUnit from './button';

function Navbar() {
    return (
        <Flex className="p-5" justify="space-between">
            <h1 className="text-burnt-green text-3xl/loose font-semibold">
                Let Them Cook 🔥
            </h1>
            <Flex justify="end">
                <ButtonUnit name="Ingredients" size="lg"/>
                <ButtonUnit name="Recipes" size="lg"/>
            </Flex>
        </Flex>
    )
}

export default Navbar