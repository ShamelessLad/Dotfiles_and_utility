/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, { enumerable: true, get: getter });
/******/ 		}
/******/ 	};
/******/
/******/ 	// define __esModule on exports
/******/ 	__webpack_require__.r = function(exports) {
/******/ 		if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 			Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 		}
/******/ 		Object.defineProperty(exports, '__esModule', { value: true });
/******/ 	};
/******/
/******/ 	// create a fake namespace object
/******/ 	// mode & 1: value is a module id, require it
/******/ 	// mode & 2: merge all properties of value into the ns
/******/ 	// mode & 4: return value when already ns object
/******/ 	// mode & 8|1: behave like require
/******/ 	__webpack_require__.t = function(value, mode) {
/******/ 		if(mode & 1) value = __webpack_require__(value);
/******/ 		if(mode & 8) return value;
/******/ 		if((mode & 4) && typeof value === 'object' && value && value.__esModule) return value;
/******/ 		var ns = Object.create(null);
/******/ 		__webpack_require__.r(ns);
/******/ 		Object.defineProperty(ns, 'default', { enumerable: true, value: value });
/******/ 		if(mode & 2 && typeof value != 'string') for(var key in value) __webpack_require__.d(ns, key, function(key) { return value[key]; }.bind(null, key));
/******/ 		return ns;
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "/";
/******/
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = "./sync/index.ts");
/******/ })
/************************************************************************/
/******/ ({

/***/ "./sync/googledrive.ts":
/*!*****************************!*\
  !*** ./sync/googledrive.ts ***!
  \*****************************/
/*! exports provided: runGoogleDriveSync, setGoogleDriveSyncEnabled, getGoogleDriveSyncEnabled */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, \"runGoogleDriveSync\", function() { return runGoogleDriveSync; });\n/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, \"setGoogleDriveSyncEnabled\", function() { return setGoogleDriveSyncEnabled; });\n/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, \"getGoogleDriveSyncEnabled\", function() { return getGoogleDriveSyncEnabled; });\nvar __awaiter = (undefined && undefined.__awaiter) || function (thisArg, _arguments, P, generator) {\n    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }\n    return new (P || (P = Promise))(function (resolve, reject) {\n        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }\n        function rejected(value) { try { step(generator[\"throw\"](value)); } catch (e) { reject(e); } }\n        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }\n        step((generator = generator.apply(thisArg, _arguments || [])).next());\n    });\n};\nvar __generator = (undefined && undefined.__generator) || function (thisArg, body) {\n    var _ = { label: 0, sent: function() { if (t[0] & 1) throw t[1]; return t[1]; }, trys: [], ops: [] }, f, y, t, g;\n    return g = { next: verb(0), \"throw\": verb(1), \"return\": verb(2) }, typeof Symbol === \"function\" && (g[Symbol.iterator] = function() { return this; }), g;\n    function verb(n) { return function (v) { return step([n, v]); }; }\n    function step(op) {\n        if (f) throw new TypeError(\"Generator is already executing.\");\n        while (_) try {\n            if (f = 1, y && (t = op[0] & 2 ? y[\"return\"] : op[0] ? y[\"throw\"] || ((t = y[\"return\"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;\n            if (y = 0, t) op = [op[0] & 2, t.value];\n            switch (op[0]) {\n                case 0: case 1: t = op; break;\n                case 4: _.label++; return { value: op[1], done: false };\n                case 5: _.label++; y = op[1]; op = [0]; continue;\n                case 7: op = _.ops.pop(); _.trys.pop(); continue;\n                default:\n                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) { _ = 0; continue; }\n                    if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) { _.label = op[1]; break; }\n                    if (op[0] === 6 && _.label < t[1]) { _.label = t[1]; t = op; break; }\n                    if (t && _.label < t[2]) { _.label = t[2]; _.ops.push(op); break; }\n                    if (t[2]) _.ops.pop();\n                    _.trys.pop(); continue;\n            }\n            op = body.call(thisArg, _);\n        } catch (e) { op = [6, e]; y = 0; } finally { f = t = 0; }\n        if (op[0] & 5) throw op[1]; return { value: op[0] ? op[1] : void 0, done: true };\n    }\n};\nvar getGoogleDriveSyncMetadata = function () {\n    return new Promise(function (resolve) {\n        chrome.storage.local.get('google-drive-sync', function (items) { return __awaiter(void 0, void 0, void 0, function () {\n            return __generator(this, function (_a) {\n                resolve(items['google-drive-sync']);\n                return [2 /*return*/];\n            });\n        }); });\n    });\n};\nvar setGoogleDriveSyncMetadata = function (googleDriveSyncMetadata) {\n    chrome.storage.local.set({ 'google-drive-sync': googleDriveSyncMetadata });\n};\nvar getOAuthAccessToken = function () {\n    return new Promise(function (resolve) {\n        chrome.identity.getAuthToken({ interactive: true }, function (token) {\n            resolve(token);\n        });\n    });\n};\nvar getGoogleDriveSyncFile = function (accessToken) {\n    return new Promise(function (resolve) { return __awaiter(void 0, void 0, void 0, function () {\n        var googleDriveSyncMetadata;\n        return __generator(this, function (_a) {\n            switch (_a.label) {\n                case 0: return [4 /*yield*/, getGoogleDriveSyncMetadata()];\n                case 1:\n                    googleDriveSyncMetadata = _a.sent();\n                    if (!googleDriveSyncMetadata) {\n                        return [2 /*return*/, resolve(null)];\n                    }\n                    fetch(\"https://www.googleapis.com/drive/v3/files/\" + googleDriveSyncMetadata.id + \"?fields=id,modifiedTime\", {\n                        method: 'GET',\n                        headers: new Headers({\n                            Authorization: \"Bearer \" + accessToken,\n                        }),\n                    })\n                        .then(function (response) { return response.json(); })\n                        .then(function (val) { return resolve(val); });\n                    return [2 /*return*/];\n            }\n        });\n    }); });\n};\nvar writeGoogleDriveSyncFile = function (accessToken, styles) {\n    return new Promise(function (resolve) {\n        var json = JSON.stringify(styles);\n        var file = new Blob([json], { type: 'application/json' });\n        var form = new FormData();\n        var metadata = {\n            name: 'stylebot_backup.json',\n            mimeType: 'application/json',\n        };\n        form.append('metadata', new Blob([JSON.stringify(metadata)], { type: 'application/json' }));\n        form.append('file', file);\n        fetch('https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart&fields=id,modifiedTime', {\n            method: 'POST',\n            headers: new Headers({\n                Authorization: \"Bearer \" + accessToken,\n            }),\n            body: form,\n        })\n            .then(function (response) { return response.json(); })\n            .then(function (_a) {\n            var id = _a.id, modifiedTime = _a.modifiedTime;\n            resolve({ id: id, modifiedTime: modifiedTime });\n        });\n    });\n};\nvar runGoogleDriveSync = function (styles) { return __awaiter(void 0, void 0, Promise, function () {\n    var accessToken, googleDriveSyncFile, _a, id, modifiedTime, id, modifiedTime;\n    return __generator(this, function (_b) {\n        switch (_b.label) {\n            case 0:\n                console.log('running google drive sync...');\n                return [4 /*yield*/, getOAuthAccessToken()];\n            case 1:\n                accessToken = _b.sent();\n                return [4 /*yield*/, getGoogleDriveSyncFile(accessToken)];\n            case 2:\n                googleDriveSyncFile = _b.sent();\n                console.log('syncing with google drive...');\n                if (!!googleDriveSyncFile) return [3 /*break*/, 4];\n                return [4 /*yield*/, writeGoogleDriveSyncFile(accessToken, styles)];\n            case 3:\n                _a = _b.sent(), id = _a.id, modifiedTime = _a.modifiedTime;\n                console.log(id, modifiedTime);\n                setGoogleDriveSyncMetadata({ id: id, modifiedTime: modifiedTime });\n                return [3 /*break*/, 5];\n            case 4:\n                console.log('updating existing sync file...');\n                id = googleDriveSyncFile.id, modifiedTime = googleDriveSyncFile.modifiedTime;\n                setGoogleDriveSyncMetadata({ id: id, modifiedTime: modifiedTime });\n                console.log(id, modifiedTime);\n                _b.label = 5;\n            case 5: return [2 /*return*/];\n        }\n    });\n}); };\nvar setGoogleDriveSyncEnabled = function (enabled) {\n    chrome.storage.local.set({ 'google-drive-sync-enabled': enabled });\n};\nvar getGoogleDriveSyncEnabled = function () {\n    return new Promise(function (resolve) {\n        chrome.storage.local.get('google-drive-sync-enabled', function (items) {\n            resolve(items['google-drive-sync-enabled'] || false);\n        });\n    });\n};\n\n\n//# sourceURL=webpack:///./sync/googledrive.ts?");

/***/ }),

/***/ "./sync/index.ts":
/*!***********************!*\
  !*** ./sync/index.ts ***!
  \***********************/
/*! exports provided: runGoogleDriveSync, getGoogleDriveSyncEnabled, setGoogleDriveSyncEnabled */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var _googledrive__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./googledrive */ \"./sync/googledrive.ts\");\n/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, \"runGoogleDriveSync\", function() { return _googledrive__WEBPACK_IMPORTED_MODULE_0__[\"runGoogleDriveSync\"]; });\n\n/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, \"getGoogleDriveSyncEnabled\", function() { return _googledrive__WEBPACK_IMPORTED_MODULE_0__[\"getGoogleDriveSyncEnabled\"]; });\n\n/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, \"setGoogleDriveSyncEnabled\", function() { return _googledrive__WEBPACK_IMPORTED_MODULE_0__[\"setGoogleDriveSyncEnabled\"]; });\n\n\n\n\n//# sourceURL=webpack:///./sync/index.ts?");

/***/ })

/******/ });