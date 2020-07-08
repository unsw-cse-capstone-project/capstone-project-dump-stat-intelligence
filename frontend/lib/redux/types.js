//auth
export const LOGIN = 'LOGIN'; //login user
export const LOGOUT = 'LOGOUT'; //logout user
export const UPDATE_DEETS = 'UPDATE_DEETS'; //update user deets
export const NEW_NEXT = 'NEW_NEXT'; //new redirect page for login modals
export const CLEAR_NEXT = 'CLEAR_NEXT'; //clear redirect page for login modals
export const ADD_FAVE = 'ADD_FAVE'; //add a fave recipe
export const REMOVE_FAVE = 'REMOVE_FAVE' //remove fave recipe

//Recipes
export const RECIPES_CLEAR = 'RECIPES_CLEAR'; //clear the recipes shown in explore page
export const RECIPES_UPDATE = 'RECIPES_UPDATE'; //query has changed, update which recipes are shown

//Explore
export const EXPLORE_CLEAR = 'EXPLORE_CLEAR'; //clear the current running list
export const EXPLORE_ADD = 'EXPLORE_ADD'; //add ingredient to running list
export const EXPLORE_REMOVE = 'EXPLORE_REMOVE'; //remove ingredient from running list
export const EXPLORE_ALL = 'EXPLORE_ALL'; //add all ingredients from pantry to running list
export const FILTER_UPDATE = 'FILTER_UPDATE'; //change state of one of the possible filters
export const FILTER_CLEAR = 'FILTER_CLEAR'; //set an filter item back to false


//pantry
export const PANTRY_GET = 'PANTRY_GET'; //user probably just logged in, retrieve their pantry
export const PANTRY_ADD = 'PANTRY_ADD'; //add item to pantry
export const PANTRY_REMOVE = 'PANTRY_REMOVE'; //remove item from pantry


//Ingredient 
export const QUERY = 'QUERY'; // new key stroke, search for new ingredient
export const CLEAR_QUERY = 'CLEAR_QUERY'; // set query back to empty

//Create
export const CLEAR_CREATE = 'CLEAR_CREATE'; // clear all the recipe info
export const LOAD_CREATE = 'LOAD_CREATE'; //load info from user to edit
export const SAVE_CREATE = 'SAVE_CREATE'; //save recipe and commit to database
export const UPDATE_CREATE = 'UPDATE_CREATE'; //update an element of the recipe
