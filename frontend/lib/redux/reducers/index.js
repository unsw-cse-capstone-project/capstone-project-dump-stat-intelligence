import { combineReducers } from 'redux';
import { authReducer } from './authReducer';
import { pantryReducer } from './pantryReducer';
import { queryReducer } from './queryReducer';
import { exploreReducer } from './exploreReducer';
import { recipesReducer } from './recipesReducer'

export default combineReducers({
    auth : authReducer,
    pantry : pantryReducer,
    query : queryReducer,
    explore : exploreReducer,
    recipes : recipesReducer

});