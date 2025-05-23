
# 🧭 Mini Hoja de Trucos de XPath para Selenium

## 1. Por **atributo exacto**
```xpath
//input[@id='username']
```
🔍 Encuentra cualquier `<input>` con `id="username"`

## 2. Por **atributo parcial** (contiene)
```xpath
//div[contains(@class, 'form')]
```
🔍 Encuentra `<div>` con una clase que contiene “form”

## 3. Por **texto exacto**
```xpath
//button[text()='Login']
```
🔍 Encuentra `<button>` con texto exacto “Login”

## 4. Por **texto parcial**
```xpath
//a[contains(text(), 'Más info')]
```
🔍 Encuentra `<a>` que contenga el texto “Más info”

## 5. Por **posición en la página**
```xpath
(//input[@type='text'])[1]
```
🔍 Primer `<input>` de tipo texto en la página

## 6. Por **jerarquía** (padre → hijo)
```xpath
//div[@class='form-group']/input
```
🔍 Encuentra `<input>` dentro de `<div class="form-group">`

## 7. Por **hermano siguiente**
```xpath
//label[text()='Email']/following-sibling::input
```
🔍 Encuentra el `<input>` que viene después de un `<label>` con texto “Email”

## 8. Por **hermano anterior**
```xpath
//input[@id='email']/preceding-sibling::label
```
🔍 Encuentra el `<label>` justo antes del `<input id="email">`

## 9. Con **múltiples condiciones**
```xpath
//input[@type='text' and @name='email']
```
🔍 `<input>` que sea de tipo texto **y** tenga `name="email"`

## 10. Por **valor del atributo que empieza con...**
```xpath
//input[starts-with(@name, 'user')]
```
🔍 Encuentra inputs con nombre que empiece por “user”

---

## 💡 Atajos útiles

| Expresión   | Significado                    |
|-------------|--------------------------------|
| `//`        | En cualquier parte del DOM     |
| `.`         | Elemento actual                |
| `..`        | Padre del elemento actual      |
| `@`         | Atributo (ej. `@id`, `@class`) |
| `*`         | Cualquier elemento             |

---

## 🧪 Probar XPath rápido en navegador

Abre DevTools (F12) y escribe en consola:

```js
$x("//button[text()='Login']")
```
