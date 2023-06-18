import { Flex } from '@chakra-ui/react'
// { recipes } is supposed to be an array of URLs, but I'm getting owned by JavaScript
import { recipes } from './searchbar'

function RecipeList() {
    return (
        <Flex justify="center">
            {recipes.map((value) =>{
                return (
                    <a href={value}>
                        <div className="text-burnt-green">
                            {value}
                        </div>
                    </a>
                )
            })}
        </Flex>
    )
}

export default RecipeList