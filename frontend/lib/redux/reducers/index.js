import { combineReducers } from 'redux';
import { authReducer } from './authReducer';
import { pantryReducer } from './pantryReducer';
import { queryReducer } from './queryReducer';
import { exploreReducer } from './exploreReducer';
import { recipesReducer } from './recipesReducer'
import { createReducer } from './createReducer';
import { expiryReducer } from './expiryReducer';

export default combineReducers({
    auth : authReducer,
    pantry : pantryReducer,
    query : queryReducer,
    explore : exploreReducer,
    recipes : recipesReducer,
    create : createReducer,
    expiry : expiryReducer,

});