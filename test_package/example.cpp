#include "Rabin.h"

int main() {
    Rabin r(0x3DA3358B4DC173LL, 53 - 8, 1024, 4096, (1 << 20)-1);
    return 0;
}
