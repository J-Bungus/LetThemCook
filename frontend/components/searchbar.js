import SearchIcon from '@mui/icons-material/Search';
import RestaurantMenuIcon from '@mui/icons-material/RestaurantMenu';
import AddIcon from '@mui/icons-material/Add';
import { useRouter } from 'next/router';
import {
    Flex,
    useDisclosure,
    Modal,
    ModalOverlay,
    ModalContent,
    ModalBody,
    ModalFooter,
    Button,
    Input,
    IconButton,
    useToast
} from '@chakra-ui/react'
import { useState } from 'react';
import axios from 'axios';

export default function SearchBar ({ data }) {
    const { isOpen, onOpen, onClose } = useDisclosure()

    // Gets ingredients from json file
    let ingredients = Object.keys(data);

    // React to make the search result filtering work
    const [filteredData, setFilteredData] = useState([]);

    const handleFilter = (event) => {
        const searchTerm = event.target.value
        const newFilter = ingredients.filter((value) => {
            return value.includes(searchTerm);
        })
        setFilteredData(newFilter);
    }

    // Temporary list holding list of user ingredients
    let tmp = []

    // Function to add ingredient to temporary list
    function addTmp(ingredient) {
        if (!tmp.includes(ingredient)) {
            tmp.push(ingredient)
        }
        console.log(tmp)
    }

    const router = useRouter();
    function redirect() {
        router.push('/recipes')
    }

    //I HATE JAVASCRIPT
    // Post request is here
    function postReq() {
        let recipes = axios.post('URL', {
            ingredients: tmp
        }).then((response) => {
            response.body
        })
        console.log("Placeholder")
    }

    return (
        <>
        {/*Button to open modal*/}
        <Flex justify="center">
            <Button 
                className="px-16 py-12"
                _hover={{
                    background: '#79c579',
                    color: 'white',
                }}
                color='#79c579' 
                onClick={onOpen} 
                leftIcon={<RestaurantMenuIcon />}
            >
                Ingredients            
            </Button>
        </Flex>
        
        {/* Modal with searchbar*/}
        <Modal isOpen={isOpen} onClose={onClose} isCentered>
            <ModalOverlay />
            <ModalContent className="fill-pale-green">
                <ModalBody>
                    <Flex justify="center" align="center" gap="10">
                        <SearchIcon className="fill-burnt-green"/>
                        <Input onChange={handleFilter} placeholder="What's cooking in your fridge?" size='lg' />
                    </Flex>
                    
                    {/* Checks search results for match with the typed in term and displays matched results*/}

                    {filteredData.length != 0 && (
                        <div className="h-96 overflow-hidden overflow-y-auto">
                            {filteredData.map((value) => {
                                return (
                                   <div className="text-burnt-green">
                                        {/* Button to add ingredient to temporary list*/}
                                        <IconButton 
                                            variant='ghost'
                                            aria-label='Add' 
                                            icon={<AddIcon />} 
                                            onClick={() => {
                                                addTmp(value);
                                            }}
                                        />
                                        {value}
                                    </div>)
                            })}
                        </div>
                    )}    
                </ModalBody>
                <ModalFooter>
                    {/* Button to make post request which sends the temporary list to backend*/}
                    <Button 
                        onClick={() => {
                            postReq();
                            redirect();
                    }}>
                        Find Recipes
                    </Button>
                </ModalFooter>
            </ModalContent>
        </Modal>
        </>
    ) 
}