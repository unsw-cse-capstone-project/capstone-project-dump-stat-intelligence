//auth
export const LOGIN = 'LOGIN'; //login user
export const LOGOUT = 'LOGOUT'; //logout user
export const UPDATE_DEETS = 'UPDATE_DEETS'; //update user deets
export const NEW_NEXT = 'NEW_NEXT'; //new redirect page for login modals
export const CLEAR_NEXT = 'CLEAR_NEXT'; //clear redirect page for login modals
export const ADD_FAVE = 'ADD_FAVE'; //add a fave recipe
export const REMOVE_FAVE = 'REMOVE_FAVE' //remove fave recipe
export const LOAD_OWNED = 'LOAD_OWNED'; // get owned recipes

//Recipes
export const RECIPES_CLEAR = 'RECIPES_CLEAR'; //clear the recipes shown in explore page
export const RECIPES_UPDATE = 'RECIPES_UPDATE'; //query has changed, update which recipes are shown
export const RECIPES_UNSUGGEST = 'RECIPES_UNSUGGEST'; //clear suggestion

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
export const PANTRY_CHANGE = 'PANTRY_CHANGE'; //Update expiry in a pantry ingredient


//Query 
export const QUERY = 'QUERY'; // new key stroke, search for new ingredient
export const CLEAR_QUERY = 'CLEAR_QUERY'; // set query back to empty

//SEARCH 
export const SEARCH = 'SEARCH'; // new key stroke, search for new ingredient
export const CLEAR_SEARCH = 'CLEAR_SEARCH'; // set SEARCH back to empty
export const SEARCH_TYPE = 'SEARCH_TYPE'; // Change the type of search

//Create
export const CLEAR_CREATE = 'CLEAR_CREATE'; // clear all the recipe info
export const LOAD_CREATE = 'LOAD_CREATE'; //load info from user to edit
export const SAVE_CREATE = 'SAVE_CREATE'; //save recipe and commit to database
export const UPDATE_CREATE = 'UPDATE_CREATE'; //update an element of the recipe
export const CAT_ADD_CREATE = 'CAT_ADD_CREATE'; // add a category to recipe
export const CAT_REMOVE_CREATE = 'CAT_REMOVE_CREATE'; // remove a category from recipe

//Expiry
export const CLEAR_EXPIRY = 'CLEAR_EXPIRY'; //Remove expiry info
export const LOAD_EXPIRY = 'LOAD_EXPIRY'; //Load expiry info
export const CHANGE_EXPIRY = 'CHANGE_EXPIRY'; //Update expiry date for ingredient 



