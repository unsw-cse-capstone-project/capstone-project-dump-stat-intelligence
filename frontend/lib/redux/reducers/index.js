import { combineReducers } from 'redux';
import { authReducer } from './authReducer';
import { pantryReducer } from './pantryReducer';
import { queryReducer } from './queryReducer';
import { exploreReducer } from './exploreReducer';
import { recipesReducer } from './recipesReducer'
import { createReducer } from './createReducer';
import { expiryReducer } from './expiryReducer';
import { searchReducer } from './searchReducer';

export default combineReducers({
    auth : authReducer,
    pantry : pantryReducer,
    query : queryReducer,
    explore : exploreReducer,
    recipes : recipesReducer,
    create : createReducer,
    expiry : expiryReducer,
    search: searchReducer,

});