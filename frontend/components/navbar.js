import { Flex } from '@chakra-ui/react';
import ButtonUnit from './button';
import Link from 'next/link';

function Navbar() {
    return (
        <Flex className="p-5" justify="space-between">
            <Link href="/#">
                <h1 className="hover:text-bush-green text-burnt-green text-3xl/loose font-semibold">
                Let Them Cook 🔥
                </h1>
            </Link>
            <Flex justify="end">
                <ButtonUnit url="/recipes" name="Saved Recipes" size="lg"/>
            </Flex>
        </Flex>
    )
}

export default Navbar